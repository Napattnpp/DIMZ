from serial import Serial
import time

text_result_path = 'Fire-Detection/Result/test-result.txt'

serialPort = '/dev/ttyUSB0'
baudRate = 115200

format_predict = ""

def main():
    # Open serial port
    with Serial(port=serialPort, baudrate=baudRate, timeout=12) as ser:
        if __name__ == "__main__":
            time.sleep(3)

        # Open file for read a prediction
        with open(text_result_path, 'r') as file:
            predict = file.readline()
            predict = predict.replace('\r', '')
            predict = predict.replace('\n', '')

            if (predict == ""):
                format_predict = format("NOD")
            else:
                format_predict = format(predict)

            # Send predict data to serial port
            print(format_predict)
            ser.write(bytes(format_predict, 'utf-8'))

def format(predict):
    return "@rp|ai$" + predict + ";"

main()