import cv2
from BB64U8.Module.bb64u8 import BB64U8

# TODO: Change serial to pyrf24

class SendImageResultModule:
    # Create an image encoder/decoder object
    bb64u8 = BB64U8()

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
        SendImageResultModule.bb64u8.encode(save_image_path, 0)

        cam.release()
        cv2.destroyAllWindows()

    def send(self):
        # Read encode image up to 32 bytes from memory
        while (chunk := SendImageResultModule.bb64u8.binary_img[:32]):
            SendImageResultModule.bb64u8.binary_img = SendImageResultModule.bb64u8.binary_img[32:]
            try:
                # Send data to serial port
                print(chunk)
            except KeyboardInterrupt:
                exit(0)