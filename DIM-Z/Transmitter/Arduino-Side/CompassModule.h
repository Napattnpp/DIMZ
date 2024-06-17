class CompassModule {
  private:
    int x, y, z;
    QMC5883LCompass compass;

  public:
    int heading;
    int azimuth;

    void init();
    void start();
    void log();
};

void CompassModule::init() {
  compass.init();
}

void CompassModule::start() {
  // Read compass values
  // This populates internal x, y, z values which can be accessed by getters
  compass.read();

  // Get azimuth
  azimuth = compass.getAzimuth();

  // Get heading
  x = compass.getX();
  y = compass.getY();
  z = compass.getZ();

  // Calculate heading
  heading = atan2(y, x) * 180 / PI;

  // Normalize to 0-360
  if (heading < 0) {
    heading += 360;
  }
}

void CompassModule::log() {
  Serial.print("\tHeading \t|\tAzimuth \n");
  Serial.print("\t" + String(heading)  + "\t\t|\t" + String(azimuth) + "\n");
  Serial.print("--------------------------------------------------------\n");
}

CompassModule compassModule;
