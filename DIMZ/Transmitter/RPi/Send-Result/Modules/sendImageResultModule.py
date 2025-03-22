import time
from pyrf24 import RF24
from pyrf24.pyrf24 import rf24_datarate_e, rf24_pa_dbm_e
import cv2
from Modules.BB64U8.Module.bb64u8 import BB64U8

class SendImageResultModule:
    # Create an image encoder/decoder object

    def __init__(self):
        self.bb64u8 = BB64U8()

        # Initialize the nrf24l01 module pin
        CE_PIN = 25
        CSN_PIN = 0

        self.radio = RF24(CE_PIN, CSN_PIN)
        if not self.radio.begin():
            print("NRF24 initialization failed!")
            exit()
        else:
            print("NRF24 initialized successfully.")

            # Set the PA level to high
            self.radio.set_pa_level(rf24_pa_dbm_e.RF24_PA_HIGH)
            self.radio.setDataRate(rf24_datarate_e.RF24_2MBPS)
            # Set the channel
            self.radio.openWritingPipe("Node1".encode('utf-8'))
            self.radio.stopListening()

            time.sleep(1)

    def getImage(self, save_image_path):
        # Select and check if camera is fine
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            print("Error: Could not open camera.")
            exit()

        # Initialize ret and frame to handle potential errors
        ret = False
        frame = None

        # Take a pictures
        for i in range(3):
            ret, frame = cam.read()
            if not ret:
                print(f"Warning: Failed to capture frame on attempt {i+1}")

        # Save image
        if ret and frame is not None:
            cv2.imwrite(save_image_path, cv2.flip(frame, 1))
            print("Image was saved.")
        else:
            print("Error: Failed to capture image.")

        # Convert image
        self.bb64u8.encode(save_image_path, 0)

        cam.release()
        cv2.destroyAllWindows()

    def loadImage(self, image_path):
        # Convert image
        self.bb64u8.encode(image_path, 0)

    def send(self):
        # Read encode image up to 32 bytes from memory
        while (self.bb64u8.binary_img):
            chunk = self.bb64u8.binary_img[:32]
            self.bb64u8.binary_img = self.bb64u8.binary_img[32:]

            try:
                if self.radio.write(chunk):  # Send the message as bytes
                    print(f"Sent {len(chunk)} bytes")
                else:
                    print("Failed to send message")
                time.sleep(0.1)  # Delay between sends
            except KeyboardInterrupt:
                print("Process interrupted. Exiting...")
                exit(0)
            except Exception as e:
                print(f"Error during transmission: {e}")