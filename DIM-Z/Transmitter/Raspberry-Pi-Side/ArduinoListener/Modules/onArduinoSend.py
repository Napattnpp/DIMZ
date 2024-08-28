import subprocess
import os

class OnArduinoSend:
    def __init__(self, ser, ai_script_path, send_textResult_path):
        self.predictionState = False

        self.ser = ser
        self.ai_script_path = ai_script_path
        self.send_textResult_path = send_textResult_path

    def onPredictionStart(self, command):
        if command == b"@ar|PR;\r\n":
            # Start predict
            self.log(0)

            # Run an AI script in background task
            process = subprocess.Popen(['python3', self.ai_script_path])
            print(f'Started process with PID: {process.pid}')

            self.setPredictionState(True)

            self.ser.write(b'@rp|AIRS$1;\r\n')

            # Secondary loop (Prediction loop)
            while self.predictionState:
                ''' Check if AI script is not running mean an object is detected. '''
                if process is None or process.poll() is not None:
                    # Stop predict
                    self.log(1)
                    self.setPredictionState(False)
                    break

                # Check if arduino send stop predict
                command = self.ser.readline()
                print(command)
                self.onPredictionStop(command, process)

            '''
                No need to kill AI-script task.
                If an object is detected the script will automaticlly exit.
            '''
            # Send prediction to Arduino
            os.system("python3 " + self.send_textResult_path)

    def onPredictionStop(self, command, process):
        if command == b"@ar|SPR;\r\n":
            # Stop predict
            self.log(1)

            # Kill python script run in background
            if process:
                process.terminate()
                process.wait()
                print(f'Stopped process with PID: {process.pid}')
            # Break from the secondary loop by @ar|SPR; command
            self.setPredictionState(False)

    def setPredictionState(self, state):
        self.predictionState = state

    def log(self, index):
        if index == 0:
            print("\n\n***********************")
            print("*    Start predict    *")
            print("***********************\n\n")
        elif index == 1:
            print("\n\n***********************")
            print("*     Stop predict    *")
            print("***********************\n\n")