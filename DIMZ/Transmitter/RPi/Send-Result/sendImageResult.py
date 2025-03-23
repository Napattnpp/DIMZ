import configparser
from Modules.sendImageResultModule import SendImageResultModule as SI

# Initialize the configparser
config = configparser.ConfigParser()
config.read('pathConfig.ini')

si = SI()
# si.loadImage(image_path=config['paths']['ai_image_result'])
si.getImage(save_image_path=config['paths']['cv2_image_result'])
si.send()