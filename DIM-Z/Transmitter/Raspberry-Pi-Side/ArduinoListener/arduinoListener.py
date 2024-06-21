from serial import Serial
import time
from Modules.onArduinoSend import OnArduinoSend

ai_script_path = 'Fire-Detection/Workspace/main.py'
send_textResult_path = 'Send-Result/sendTextResult.py'

serialPort = '/dev/ttyUSB0'
baudRate = 115200

def main():
    # Open serial port
    with Serial(port=serialPort, baudrate=baudRate, timeout=12) as ser:
        onArduinoSend = OnArduinoSend(ser, ai_script_path, send_textResult_path)
        time.sleep(3)

        try:
            # Primary loop (Loop check data from arduino)
            while True:
                command = ser.readline()
                print(command)
                onArduinoSend.onPredictionStart(command)
        except Exception:
            exit(0)

if __name__ == "__main__":
    main()
