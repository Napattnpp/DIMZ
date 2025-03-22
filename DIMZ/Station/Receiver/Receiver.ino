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
  // Start serial communication for debugging
  Serial.begin(115200);

  // Initialize NRF24
  if (!radio.begin()) {
    Serial.println("Error: Radio hardware not found.");
    while (1);  // Halt the program if the NRF24L01 module is not found
  }
  radio.openReadingPipe(0, address);  // Open the reading pipe
  radio.setPALevel(RF24_PA_HIGH);  // Max power for range
  radio.setDataRate(RF24_2MBPS);  // Reliable transmission speed
  radio.startListening();  // Start listening for incoming data

  Serial.println("Receiver Ready. \nWaiting for image data...");
}

void loop() {
  if (radio.available()) {
    // Create a buffer to hold the incoming data
    byte receivedData[32];
    radio.read(receivedData, sizeof(receivedData));

    // Check for the end of image marker
    if (memcmp(receivedData, "!EOF", 4) == 0) {
      Serial.println("End of image received.");
    } else {
      // Print received data (for debugging purposes)
      // Serial.print("Received chunk: ");
      for (int i = 0; i < 32; i++) {
        Serial.print(receivedData[i], HEX);
        Serial.print(" ");
      }
      Serial.println();
    }
  }
}
