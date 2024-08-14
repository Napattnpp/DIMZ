class ServoModule {
  private:
    Servo servo;
    int state;
    bool writingState;

  public:
    ServoModule() {
      state = -1;
      writingState = false;
    }

    void init();
    void resolution360();
};

void ServoModule::init() {
  servo.attach(SERVO_PIN);

  Serial.println("[ServoModule]: Setting up servo");

  // Set Servo (camera) angle with compass
  while (true) {
    compassModule.start();

    if (abs(abs(compassModule.azimuth) - 5) <= COMPASS_OFFSET) {
      break;
    }

    if (compassModule.azimuth > 0) {
      servo.write(SERVO_COUNTER_CLOCKWISE);
    } else if (compassModule.azimuth < 0) {
      servo.write(SERVO_CLOCKWISE);
    }
  }

  state = 0;
  servo.write(SERVO_STOP);
  Serial.println("[ServoModule]: Setup successfully");
}

void ServoModule::resolution360() {
  compassModule.start();

  switch (state) {
    case 0:
      if (abs(abs(compassModule.azimuth) - 180) >= COMPASS_OFFSET) {
        if (writingState == false) {
          SAW("@ar|PR;\r\n", "@rp|AIRS$1\r\n");
          // Serial.println("[ServoModule]: (state) 0");
          servo.write(SERVO_CLOCKWISE);
          state = 0;
          writingState = true;
        }
      } else {
        servo.write(SERVO_STOP);
        state = 1;
        writingState = false;
      }
      break;

    case 1:
      if (abs(compassModule.azimuth) >= COMPASS_OFFSET) {
        if (writingState == false) {
          // Serial.println("[ServoModule]: (state) 1");
          servo.write(SERVO_CLOCKWISE);
          state = 1;
          writingState = true;
        }
      } else {
        servo.write(SERVO_STOP);
        state = 2;
        writingState = false;
      }
      break;

    case 2:
      if (abs(abs(compassModule.azimuth) - 180) >= COMPASS_OFFSET) {
        if (writingState == false) {
          // Serial.println("[ServoModule]: (state) 2");
          servo.write(SERVO_COUNTER_CLOCKWISE);
          state = 2;
          writingState = true;
        }
      } else {
        servo.write(SERVO_STOP);
        state = 3;
        writingState = false;
      }
      break;

    case 3:
      if (abs(compassModule.azimuth) >= COMPASS_OFFSET) {
        if (writingState == false) {
          // Serial.println("[ServoModule]: (state) 3");
          servo.write(SERVO_COUNTER_CLOCKWISE);
          state = 3;
          writingState = true;
        }
      } else {
        servo.write(SERVO_STOP);
        state = 4;
        writingState = false;
      }
      break;

    case 4:
      if (writingState == false) {
        Serial.println("@ar|SPR;\r\n");
        // Serial.println("[ServoModule]: (state) 4");
        servo.write(SERVO_STOP);
        writingState = true;
      }
      break;
  
  }
}

ServoModule servoModule;
