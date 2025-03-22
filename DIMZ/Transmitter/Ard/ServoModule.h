class ServoModule {
  private:
    Servo servo;
    int servo_pin = 0;

  public:
    ServoModule(int _pin) {
      servo_pin = _pin;
    }

    void init();
    bool start();
};

void ServoModule::init() {
  servo.attach(servo_pin);
}

bool ServoModule::start() {
  SAW("@ar|PR;\r\n", "@rp|AIRS$1;\r\n");

  for (int i = 0; i < 180; i++) {
    servo.write(i);
    delay(100);
  }

  for (int i = 180; i > 0; i--) {
    servo.write(i);
    delay(100);
  }

  Serial.println("@ar|SPR;\r\n");

  return true;
}
