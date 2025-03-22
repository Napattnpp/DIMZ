from serial import Serial
import time

serial_port = '/dev/tty.usbmodem1101'

def fillter(buffer):
    # Replace all instances of \r\n with just \n
    return buffer.replace(b'\r\n', b'')

def readDate(port, baudRate, filePath):
  time.sleep(3)

  print("[Executing]")
  # Read data from serial port
  with Serial(port=port, baudrate=baudRate, timeout=12) as ser:

    # Save data to file
    with open(filePath, 'wb') as file:
      while (buffer := ser.read()):
        # Clean the data
        buffer = fillter(buffer)

        print(buffer)
        file.write(buffer)

  print("[Done]")

if __name__ == "__main__":
  readDate(serial_port, 115200, 'DIMZ/Station/Output/image-output-serial.txt')
