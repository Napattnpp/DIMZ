from serial import Serial
import subprocess
import sys
import time

ai_script_path = 'Fire-Detection/Workspace/main.py'
send_textResult_path = 'Send-Result/sendTextResult.py'

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
                log(0)

                while True:
                    # Run an AI script in background task
                    process = subprocess.Popen(['python3', ai_script_path])
                    print(f'Started process with PID: {process.pid}')

                    '''
                        Check if AI script is not running mean
                        an object is detected.
                    '''
                    if process == False:
                        # Stop predict
                        log(1)
                        break

                    command = ser.readline()
                    print(command)
                    if command == b"@ar|pred$-1;\r\n":
                        # Stop predict
                        log(1)
                        # Kill python script run in background
                        if process:
                            # Sends SIGTERM to the process
                            process.terminate()
                            # Wait for process to terminate
                            process.wait()
                            print(f'Stopped process with PID: {process.pid}')
                        # Break from the predict loop by @ar|pred$-1; command
                        break
                '''
                    Break from the predict loop if object is detected.
                    No need to kill AI-script task.
                    If an object is detected the script will automatic exist.
                '''
                break
        # Send prediction to Arduino
        sys.os("python3 " + send_textResult_path)

def log(index):
    if index == 0:
        print("\n\n***********************")
        print("*    Start predict     *")
        print("***********************\n\n")
    elif index == 1:
        print("\n\n***********************")
        print("*     Stop predict     *")
        print("***********************\n\n")

if __name__ == "__main__":
    main()
