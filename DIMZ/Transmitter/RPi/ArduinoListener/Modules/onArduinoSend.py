import subprocess
import os

class OnArduinoSend:
    def __init__(self, ser, ai_script_path, sendImageResult_path):
        self.prediction_state = False
        self.detection_exit = False

        self.ser = ser
        self.ai_script_path = ai_script_path
        self.sendImageResult_path = sendImageResult_path

    def onPredictionStart(self, command):
        if command == b"@ar|PR;\r\n":
            # Start predict
            self.log(0)

            # Run an AI script in background task
            process = subprocess.Popen(['python3', self.ai_script_path])
            print(f'Start process with PID: {process.pid}')

            self.prediction_state = True

            self.ser.write(b'@rp|AIRS$1;\r\n')

            # Secondary loop (Prediction loop)
            while self.prediction_state:
                ''' Check if the AI script is not running, which means an object is detected. '''
                if process is None or process.poll() is not None:
                    # Stop predict
                    self.log(1)
                    self.prediction_state = False
                    self.detection_exit = True
                    break

                # Check if arduino send stop predict
                command = self.ser.readline()
                print(command)
                self.onPredictionStop(command, process)

            '''
                No need to kill the AI-script task.
                If an object is detected the script will automatically exit.

                If AI script exits by detection --> execute sendImageResult
            '''
            # Send prediction to Arduino
            if self.detection_exit:
                os.system("python3 " + self.sendImageResult_path)

    def onPredictionStop(self, command, process):
        if command == b"@ar|SPR;\r\n":
            # Stop predict
            self.log(1)

            # Kill Python script run in the background
            if process:
                process.terminate()
                process.wait()
                print(f'Stopped process with PID: {process.pid}')

            # TODO: Write text-result.txt --> Not detect
            # Break from the secondary loop by @ar|SPR; command
            self.prediction_state = False
            self.detection_exit = False

    def log(self, index):
        if index == 0:
            print("\n\n***********************")
            print("*    Start predict    *")
            print("***********************\n\n")
        elif index == 1:
            print("\n\n***********************")
            print("*     Stop predict    *")
            print("***********************\n\n")
