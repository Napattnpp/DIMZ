import config
from Modules.sendTextResultModule import SendTextResultModule as ST

st = ST(config.SERIAL_PORT, config.BAUD_RATE)
st.start()
st.sendFromFile(text_result_path=config.AI_TEXT_RESULT_PATH)