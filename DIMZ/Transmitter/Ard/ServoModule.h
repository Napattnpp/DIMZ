class ServoModule {
  private:
    Servo servo;
    int servo_pin = 0;

    bool detectionExit();

  public:
    bool start_state = true;

    ServoModule(int _pin) {
      servo_pin = _pin;
    }

    void init();
    void start();
};

bool ServoModule::detectionExit() {
  if (Serial.available() > 0) {;
    if (Serial.readString() == "@rp|DETE$1;\r\n") {
      start_state = false;
      return 1;
    }
  }

  return 0;
}

void ServoModule::init() {
  servo.attach(servo_pin);
  delay(50);
  servo.write(90);
}

void ServoModule::start() {
  if (start_state == false) return;
  if (SAW("@ar|PREP;\r\n", "@rp|SRS$1;\r\n") == false) return;

  for (int i = 0; i < 180; i++) {
    if (detectionExit()) { return; }
    servo.write(i);
    delay(100);
  }

  for (int i = 180; i > 0; i--) {
    if (detectionExit()) { return; }
    servo.write(i);
    delay(100);
  }

  Serial.println("@ar|SPR;\r\n");

  start_state = false;
}
