import configparser
from Modules.sendTextResultModule import SendTextResultModule as ST

# Initialize the configparser
config = configparser.ConfigParser()
config.read('pathConfig.ini')

st = ST(config['serial_info']['serial_port'], config['serial_info']['baud_rate'])
st.start()
st.sendFromFile(text_result_path=config['paths']['ai_text_result'])