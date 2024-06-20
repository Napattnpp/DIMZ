from serial import Serial
import time

serialPort = '/dev/ttyUSB0'
baudRate = 115200
text_result_path = './Fire-Detection/Result/test-result.txt'

def main():
    # Open serial port
    with Serial(port=serialPort, baudrate=baudRate, timeout=12) as ser:
        time.sleep(3)

        # Open file for read a prediction
        with open(text_result_path, 'r') as file:
            predict = file.readline().split()

            # Send predict data to serial port
            print("@rp|ai$" + predict + ";")
            ser.write("@rp|ai$" + predict + ";")

main()