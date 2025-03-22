class ServoModule {
  private:
    Servo servo;
    int servo_pin = 0;

  public:
    bool start_state = true;

    ServoModule(int _pin) {
      servo_pin = _pin;
    }

    void init();
    void start();
};

void ServoModule::init() {
  servo.attach(servo_pin);
}

void ServoModule::start() {
  if (start_state == false) return;
  if (SAW("@ar|PR;\r\n", "@rp|AIRS$1;\r\n") == false) return;

  for (int i = 0; i < 180; i++) {
    servo.write(i);
    delay(100);
  }

  for (int i = 180; i > 0; i--) {
    servo.write(i);
    delay(100);
  }

  Serial.println("@ar|SPR;\r\n");

  start_state = false;
}
