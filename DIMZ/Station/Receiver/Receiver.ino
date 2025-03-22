#include <SPI.h>
#include <RF24.h>

// Define the NRF24L01 CE and CSN pins
#define CE_PIN   9
#define CSN_PIN 10

// Create an RF24 object
RF24 radio(CE_PIN, CSN_PIN);

// Define the receiver's pipe address (must match the sender's address)
uint8_t address[6] = "Node1";

void setup() {
  Serial.begin(115200);

  // Initialize NRF24
  if (!radio.begin()) {
    Serial.println("Error: Radio hardware not found.");
    while (1);
  }
  radio.openReadingPipe(0, address);  // Open the reading pipe
  radio.setPALevel(RF24_PA_HIGH);     // Max power for range
  radio.setDataRate(RF24_2MBPS);      // Reliable transmission speed
  radio.startListening();             // Start listening for incoming data
}

void loop() {
  if (radio.available()) {
    // Get the size of the payload (data received)
    int payloadSize = radio.getDynamicPayloadSize();
    byte data[payloadSize];

    // Read the received data
    radio.read(data, payloadSize);
    
    // Print the received data
    for (int i = 0; i < payloadSize; i++) {
      Serial.print(data[i], HEX);
      Serial.print(" ");
    }
    Serial.println();
  }
}
