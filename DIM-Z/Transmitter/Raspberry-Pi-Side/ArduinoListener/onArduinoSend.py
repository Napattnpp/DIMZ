from serial import Serial
import subprocess
import time

ai_script_path = './Fire-Detection/Workspace/main.py'

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
                    # Run an AI script in background task
                    process = subprocess.Popen(['python3', ai_script_path])
                    print(f'Started process with PID: {process.pid}')

                    command = ser.readline()
                    print(command)
                    if command == b"@ar|pred$-1;\r\n":
                        # Stop predict
                        print("\n\n***********************")
                        print("*     Stop predict     *")
                        print("***********************\n\n")
                        # Kill python script run in background
                        if process:
                            # Sends SIGTERM to the process
                            process.terminate()
                            # Wait for process to terminate
                            process.wait()
                            print(f'Stopped process with PID: {process.pid}')
                        break
                break

if __name__ == "__main__":
    main()
