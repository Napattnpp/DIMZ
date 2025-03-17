import config
import time
from serial import Serial
from Modules.onArduinoSend import OnArduinoSend

def main():
    # Open serial port
    with Serial(port=config.SERIAL_PORT, baudrate=config.BAUD_RATE, timeout=12) as ser:
        onArduinoSend = OnArduinoSend(ser, config.AI_SCRIPT_PATH, config.SEND_TEXT_RESULT_PATH)
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
