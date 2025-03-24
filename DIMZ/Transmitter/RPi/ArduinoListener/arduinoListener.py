import configparser
import time
from serial import Serial
from Modules.onArduinoSend import OnArduinoSend

# Initialize the configparser
config = configparser.ConfigParser()
config.read('pathConfig.ini')

def main():
    # Open serial port
    with Serial(port=config['serial_info']['serial_port'], baudrate=config['serial_info']['baud_rate'], timeout=12) as ser:
        onArduinoSend = OnArduinoSend(ser, config['paths']['ai_script'], config['paths']['send_image_result'])
        time.sleep(2)

        try:
            # Primary loop (Loop check data from Arduino)
            while True:
                if ser.in_waiting > 0:
                    command = ser.readline()
                    print(command)
                    onArduinoSend.onPredictionStart(command)

                time.sleep(0.01)
        except Exception:
            exit(0)

if __name__ == "__main__":
    main()
