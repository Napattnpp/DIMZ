class ServoModule {
  private:
    Servo servo;

    unsigned long ct = 0;
    unsigned long pt = 0;

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
  bool s = 0;

  servo.attach(SERVO_PIN);

  Serial.println("[ServoModule]: Setting up servo");

  // Set Servo (camera) angle with compass
  while (true) {
    compassModule.start();

    if (abs(abs(compassModule.azimuth) - 5) <= COMPASS_OFFSET_1) {
      break;
    }

    if (compassModule.azimuth > 0) {
      if (writingState == false) {
        servo.write(SERVO_COUNTER_CLOCKWISE);

        s = 0;
        writingState == true;
      } else if (writingState == false && s == 1) {
        writingState == true;
      }
    } else if (compassModule.azimuth < 0) {
      if (writingState == false) {
        servo.write(SERVO_CLOCKWISE);

        s = 1;
        writingState == true;
      } else if (writingState == false && s == 0) {
        writingState == true;
      }
    }

    delay(100);
  }

  state = 0;
  writingState = false;

  servo.write(SERVO_STOP);
  Serial.println("[ServoModule]: Setup successfully");
}

void ServoModule::resolution360() {
  compassModule.start();
  // compassModule.log();

  switch (state) {
    case 0:
      if (abs(abs(compassModule.azimuth) - 180) >= COMPASS_OFFSET_1) {
        if (writingState == false) {
          SAW("@ar|PR;\r\n", "@rp|AIRS$1;\r\n");
          Serial.println("[ServoModule]: (state) 0");
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
      if (abs(compassModule.azimuth) >= COMPASS_OFFSET_1) {
        if (writingState == false) {
          Serial.println("[ServoModule]: (state) 1");
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
      if (abs(abs(compassModule.azimuth) - 180) >= COMPASS_OFFSET_1) {
        if (writingState == false) {
          Serial.println("[ServoModule]: (state) 2");
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
      if (abs(compassModule.azimuth) >= COMPASS_OFFSET_1+COMPASS_OFFSET_2) {
        if (writingState == false) {
          Serial.println("[ServoModule]: (state) 3");
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
        Serial.println("[ServoModule]: (state) 4");
        servo.write(SERVO_STOP);
        writingState = true;

        pt = millis();
      } else {
        ct = millis();

        // Waiting for 30 second
        if (ct - pt >= 30000) {
          state = 0;
          writingState = false;
        }
      }
      break;
  }
}

ServoModule servoModule;
