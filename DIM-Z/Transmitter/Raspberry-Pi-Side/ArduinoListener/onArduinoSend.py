from serial import Serial
import time
import cv2

serialPort = '/dev/ttyUSB0'
baudRate = 115200

video_output_path = ''

camera = cv2.VideoCapture(0)

# Get frame size
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_output_path, fourcc, 20, frame_size)

def main():
    # Open serial port
    with Serial(port=serialPort, baudrate=baudRate, timeout=12) as ser:
        time.sleep(3)

        # Loop check data from arduino
        while True:
            command = ser.readline()
            print(command)
            if command == b"@ar|rec$1;\r\n":
                # Start record
                print("\n\n***********************")
                print("*    Start record    *")
                print("***********************\n\n")
                ret, frame = camera.read()

                while camera.isOpened():

                    command = ser.readline()
                    print(command)

                    # TODO: Write frame
                    out.write(frame)

                    if command == b"@ar|rec$-1\r\n":
                        # Stop record
                        print("\n\n***********************")
                        print("*    Stop record     *")
                        print("***********************\n\n")
                        break
                out.release()
                camera.release()

                # TODO: Call AI

if __name__ == "__main__":
    main()

