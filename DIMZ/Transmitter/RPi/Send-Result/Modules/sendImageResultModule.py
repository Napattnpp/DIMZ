import time
import sys
from pyrf24 import RF24
from pyrf24.pyrf24 import rf24_datarate_e, rf24_pa_dbm_e
import cv2
from Modules.BB64U8.Module.bb64u8 import BB64U8

class SendImageResultModule:
    # Create an image encoder/decoder object

    def __init__(self):
        # Initialize the nrf24l01 module pin
        CE_PIN = 25
        CSN_PIN = 0

        self.bb64u8 = BB64U8()
        self.package_size = 0

        self.radio = RF24(CE_PIN, CSN_PIN)
        if not self.radio.begin():
            print("NRF24 initialization failed!")
            sys.exit(0)
        else:
            print("NRF24 initialized successfully.")

            # Set the PA level to high
            self.radio.set_pa_level(rf24_pa_dbm_e.RF24_PA_HIGH)
            self.radio.setDataRate(rf24_datarate_e.RF24_2MBPS)

            # Ensure dynamic payloads are on
            self.radio.enableDynamicPayloads()
            # Enable auto-ack (required for dynamic payloads)
            self.radio.setAutoAck(True)

            # Set the channel
            self.radio.openWritingPipe("Node1".encode('utf-8'))
            self.radio.stopListening()

            time.sleep(1)

    def getImage(self, save_image_path):
        # Select and check if camera is fine
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            print("Error: Could not open camera.")
            sys.exit(0)

        # Initialize ret and frame to handle potential errors
        ret = False
        frame = None

        # Take a pictures
        for i in range(5):
            ret, frame = cam.read()
            if not ret:
                print(f"Warning: Failed to capture frame on attempt {i+1}")

        # Save image
        if ret and frame is not None:
            cv2.imwrite(save_image_path, frame)
            print("Image was saved.")
        else:
            print("Error: Failed to capture image.")
            cam.release()
            sys.exit(0)

        # Release the camera
        cam.release()

        # Convert image
        self.bb64u8.encode(save_image_path, 0)

    def loadImage(self, image_path):
        # Convert image
        self.bb64u8.encode(image_path, 0)

    def handle_exit(self):
        self.radio.powerDown()
        sys.exit(0)

    def send(self):
        print("Transmitting is starting...")

        # Read encode image up to 32 bytes from memory
        while (self.bb64u8.binary_img):
            # Read the first 32 bytes from the memory
            chunk = self.bb64u8.binary_img[:32]
            # Remove the first 32 bytes from the memory
            self.bb64u8.binary_img = self.bb64u8.binary_img[32:]

            try:
                if self.radio.write(chunk):  # Send the message as bytes
                    # print(chunk)
                    # print(f"({len(chunk)} bytes)")
                    self.package_size = self.package_size + 1
                else:
                    print("Failed to send message")
                    exit(1)
            except KeyboardInterrupt:
                print("Process interrupted. Exiting...")
                self.handle_exit()
            except Exception as e:
                print(f"Error during transmission: {e}")
                self.handle_exit()

        # Send the EOF message (optional)
        # self.radio.write(b'!')
        print(f"Transmission completed with Package size: {self.package_size}")
        self.radio.powerDown()