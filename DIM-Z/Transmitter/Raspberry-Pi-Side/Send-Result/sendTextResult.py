from Modules.sendTextResultModule import SendTextResultModule as st

text_result_path = 'Fire-Detection/Result/test-result.txt'

serialPort = '/dev/ttyACM0'
baudRate = 115200

st.start()
st.sendFromFile(text_result_path=text_result_path)