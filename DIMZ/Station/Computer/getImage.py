import serial

# This function is used to remove the \r\n from the buffer (optional)
def fillter(buffer):
  # Replace all instances of \r\n with just \n
  return buffer.replace(b'\r\n', b'')

def save_image(port, baud_rate, output_path):
  # Open the serial port
  ser = serial.Serial(port, baud_rate, timeout=12)

  open_file_status = False

  while True:
    # Read the first 32 bytes from the serial port
    while chunk := ser.read(32):
      # Check if the file is not open
      if not open_file_status:
        img_file = open(output_path, 'wb')
        open_file_status = True

        # Print the chunk
        print(chunk)
        img_file.write(chunk)

    if open_file_status:
      img_file.close()
      open_file_status = False
      print("[Image Received]")

    print("[Waiting for New Data...]")

save_image('/dev/tty.usbmodem1101', 115200, 'received_image.jpg')
