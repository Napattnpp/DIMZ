import pathConfig
from Modules.sendTextResultModule import SendTextResultModule as ST

st = ST(pathConfig.SERIAL_PORT, pathConfig.BAUD_RATE)
st.start()
st.sendFromFile(text_result_path=pathConfig.AI_TEXT_RESULT_PATH)