from serial import Serial
import os
import sys
import time

video_output_path = './Fire-Detection/Image/Source/video-output.mp4'
ai_path = './Fire-Detection/Workspace/main.py'

serialPort = '/dev/ttyUSB0'
baudRate = 115200

def main():
    # Open serial port
    with Serial(port=serialPort, baudrate=baudRate, timeout=12) as ser:
        time.sleep(3)

        # Loop check data from arduino
        while True:
            command = ser.readline()
            print(command)
            if command == b"@ar|pred$1;\r\n":
                # Start predict
                print("\n\n***********************")
                print("*    Start predict     *")
                print("***********************\n\n")

                while True:
                    # Run an AI in background task
                    os.system('python3 ' + ai_path + " &")

                    command = ser.readline()
                    print(command)
                    if command == b"@ar|pred$-1;\r\n":
                        # Stop predict
                        print("\n\n***********************")
                        print("*     Stop predict     *")
                        print("***********************\n\n")
                        # Kill python script run in background
                        break
                break

if __name__ == "__main__":
    main()