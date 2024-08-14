from serial import Serial
import time

def clean_data(buffer):
    # Replace all instances of \r\n with just \n
    return buffer.replace(b'\r\n', b'')

def Getting(port, baudRate, filePath):
  time.sleep(3)

  print("[Executing]")
  # Read data from serial port
  with Serial(port=port, baudrate=baudRate, timeout=12) as ser:

    # Save data to file
    with open(filePath, 'wb') as file:
      while (buffer := ser.read(32)):
        # Clean the data
        buffer = clean_data(buffer)
        
        print(buffer)
        file.write(buffer)

  print("[Done]")

if __name__ == "__main__":
  Getting('/dev/tty.usbmodem14101', 115200, 'DIM-Z/Station/Output/image-output-serial.txt')
