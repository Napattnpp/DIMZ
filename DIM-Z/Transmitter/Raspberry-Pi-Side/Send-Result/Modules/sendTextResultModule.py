from serial import Serial
import time

class SendTextResultModule:
    def __init__(self, serialPort, baudRate):
        self.serialPort = serialPort
        self.baudRate = baudRate

    def start(self):
        # Open serial port
        with Serial(port=self.serialPort, baudrate=self.baudRate, timeout=12) as ser:
            if __name__ == "__main__":
                time.sleep(3)

    def sendFromFile(self, text_result_path):
        format_predict = ""

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
            self.ser.write(bytes(format_predict, 'utf-8'))

    def format(predict):
        return "@rp|ai$" + predict + ";"