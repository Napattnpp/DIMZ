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
        time.sleep(3)

        try:
            # Primary loop (Loop check data from Arduino)
            while True:
                command = ser.readline()
                print(command)
                onArduinoSend.onPredictionStart(command)
        except Exception:
            exit(0)

if __name__ == "__main__":
    main()
