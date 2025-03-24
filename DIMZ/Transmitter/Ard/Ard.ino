#include "SystemFile.h"

DHTX dhtx(DHT_PIN, DHT_TYPE);
MQX mqx(MQX_PIN);
GPSModule gps;
ServoModule servoModule(SERVO_PIN);

unsigned long currentTime = 0;
unsigned long previousTime[2];

void setup() {
  Serial.begin(115200);
  delay(100);

  servoModule.init();
  gps.init();
  mqx.init();
  dhtx.init();
}

void loop() {
  main_task();
}

void main_task() {
  currentTime = millis();

  //--------------------------------------------------------------------- Collect and Send data to datacenter ---------------------------------------------------------------------//
  // Read & Send data every 30 minute
  if (currentTime - previousTime[0] >= 30 * 60000) {
    // Get temp, humidity, co, lpg and smoke value
    mqx.get();
    dhtx.get();

    mqx.log();
    dhtx.log();

    // Get current location
    gps.getCoordinate();

    previousTime[0] = currentTime;
  }

  // Start servo motor every 3 minute
  servoModule.start();
  if (currentTime - previousTime[1] >= 3 * 60000) {
    servoModule.start_state = true;
    previousTime[1] = currentTime;
  }

  delay(100);
}