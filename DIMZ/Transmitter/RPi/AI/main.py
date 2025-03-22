import configparser
import sys
import cv2
from ultralytics import YOLO

# Initialize the configparser
config = configparser.ConfigParser()
config.read('pathConfig.ini')
ai_image_result_path = config['paths']['ai_image_result']
ai_text_result_path = config['paths']['ai_text_result']

# Custom class mapping (modify as needed)
class_mapping = {
    0: "@rp|ai$FID;",
    1: "@rp|ai$SID;"
}

# Load NCNN model
ncnn_model = YOLO(config['ncnn_paths']['model_path'], task='detect')

def __main__():
# Process results and save to a text file (overwrite previous)
while (1):
    # Start detection from webcam and MUST use stream=True for real-time processing
    results = ncnn_model.predict(source=0, stream=True, conf=0.83)

    for result in results:
        # Check if any detection is made
        if result.boxes is not None and len(result.boxes) > 0:
            print("Detection Found!")

            # Process and save detected classes
            with open(ai_text_result_path, 'w') as file:
                for box in result.boxes:
                    # Get bounding box coordinates (x1, y1, x2, y2)
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    # Save image result
                    cv2.imwrite(ai_image_result_path, result.orig_img[y1:y2, x1:x2])
                    print(f"Saved: {ai_image_result_path}")

                    # Save text result
                    # box.cls() -> Return the class values of the boxes.
                    class_id = int(box.cls[0])
                    detected_label = class_mapping.get(class_id, f"unknown_{class_id}")
                    file.write(detected_label)

            print(f"Results saved to {ai_text_result_path}")
            sys.exit(0)
