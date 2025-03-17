import base64

class BB64U8:
    def __intit__(self):
        self.binary_img = ""
        self.base64_img = ""

        # Use for printing on the screen
        self.utf8_img = ""

        self.decode_img = ""

    def encode(self, img_path):
        with open(img_path, "rb") as img_file:
            # Read the binary data of the image
            self.binary_img = img_file.read()
            # Encode the image data to Base64
            self.base64_img = base64.b64encode(self.binary_img)

            # Convert to string format for transmission
            self.utf8_img = self.base64_img.decode("utf-8")

    def saveTextImg(self, file_path, textImage):
        with open(file_path, "wb") as file:
            file.write(textImage)

    def decode(self, save_path, encodedImg):
        # Decode the Base64 back to binary data
        self.decode_img = base64.b64decode(encodedImg)

        # Save the decoded image to verify
        with open(save_path, "wb") as file:
            file.write(self.decode_img)
