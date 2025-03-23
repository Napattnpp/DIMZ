import serial

# This function is used to remove the \r\n from the buffer (optional)
def fillter(buffer):
  # Replace all instances of \r\n with just \n
  return buffer.replace(b'\r\n', b'')

def save_image(port, baud_rate, output_path):
  # Open the serial port
  ser = serial.Serial(port, baud_rate, timeout=12)

  # Open the output file
  with open(output_path, 'wb') as img_file:
    while True:
      while chunk := ser.read(32):
        print(chunk)
        img_file.write(chunk)
      print("[Waiting for New Data...]")

save_image('/dev/tty.usbmodem1101', 115200, 'received_image.jpg')
