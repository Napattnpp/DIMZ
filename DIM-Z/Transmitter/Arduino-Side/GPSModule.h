class GPSModule {
  private:
    bool skipPinState = 0;
    
    TinyGPSPlus tinyGps;
    // SoftwareSerial GPSSerial;

  public:
    double latitude = 0.0;
    double longitude = 0.0;

    // GPSModule() : GPSSerial(GPS_RX_PIN, GPS_TX_PIN) {};
    
    void init();
    void rawCommand();
    void getCoordinate();
};

void GPSModule::init() {
  pinMode(GPS_SKIP_PIN, INPUT_PULLUP);

  Serial.println("GPS-Serial begin at 9600 baud");
  Serial.print("Waiting for satellites");
  while (tinyGps.satellites.value() < 3) {
    Serial.print(".");

    if (!digitalRead(GPS_SKIP_PIN)) {
      skipPinState = 1;
      break;
    }

    delay(300);
  }
  Serial.println("");

  if (skipPinState) {
    Serial.println("[Task was skipped]");
    delay(1000);
  }

  Serial.print("Number of satellites: ");
  Serial.println(tinyGps.satellites.value());
}

void GPSModule::rawCommand() {
  if (Serial.available()) {
    Serial2.write(Serial.read());
  }
  if (Serial2.available()) {
    Serial.write(Serial2.read());
  }
}

void GPSModule::getCoordinate() {
  if (Serial2.available()) {
    tinyGps.encode(Serial2.read());

    latitude = tinyGps.location.lat(), 6;
    longitude = tinyGps.location.lng(), 6;
  }
}

GPSModule gps;
