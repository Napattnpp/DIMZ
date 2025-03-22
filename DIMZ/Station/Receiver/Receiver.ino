#include <RF24.h>

#define CE          9
#define CSN         10

const unsigned char address[] = "Node1";
RF24 radio(CE, CSN);

void setup() {
  Serial.begin(115200);

  Serial.println(F("[MyNRF]: Setting up receiver"));
  // Initialize the transceiver on the SPI bus
  if (!radio.begin()) {
    Serial.println(F("[MyNRF]: Radio hardware is not responding!!"));
    // Hold in infinite loop
    while (1);
  }

  radio.openReadingPipe(0, address);

  radio.setPALevel(RF24_PA_HIGH);
  radio.setDataRate(RF24_2MBPS);

  radio.startListening();

  // Serial.println(F("[MyNRF]: Setup finished"));
}

void loop() {
  if (radio.available()){
    char text[32] = "";

    radio.read(&text, sizeof(text));
    Serial.println(text);
  }
}
