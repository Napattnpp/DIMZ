import configparser
from Modules.sendImageResultModule import SendImageResultModule as SI

# Initialize the configparser
config = configparser.ConfigParser()
config.read('pathConfig.ini')

si = SI(config['serial_info']['serial_port'], config['serial_info']['baud_rate'])
si.loadImage(image_path=config['paths']['ai_image_result'])
si.send()