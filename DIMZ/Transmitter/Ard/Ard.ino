#include "pico/multicore.h"
#include "SystemFile.h"

DHTX dhtx(DHT_PIN, DHT_TYPE);
MQX mqx(MQX_PIN);
GPSModule gps;
ServoModule servoModule(SERVO_PIN);

unsigned long currentTime = 0;
unsigned long previousTime[2];

// Function to run on Core 1
void core1Task() {
  while (true) {
    if (servoModule.start()) {
      delay(2 * 60000);
    }

    delay(100);
  }
}

void setup() {
  Serial.begin(115200);
  delay(3000);

  servoModule.init();

  gps.init();

  //! Initialize dht the last one !//
  mqx.init();
  dhtx.init();

  // Launch core1Task() on Core 1
  multicore_launch_core1(core1Task);
}

void loop() {
  main_task();
}

void main_task() {
  currentTime = millis();

  //--------------------------------------------------------------------- Collect and Send data to datacenter ---------------------------------------------------------------------//
  // Read & Send data every 30 minute
  if (currentTime - previousTime[0] >= 30 * 10000 ) {
    // Get temp, humidity, co, lpg and smoke value
    mqx.get();
    dhtx.get();

    mqx.log();
    dhtx.log();

    // Get current location
    gps.getCoordinate();

    previousTime[0] = currentTime;
  }

  delay(100);
}