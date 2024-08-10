class MyNRF {
  private:
    RF24 radio;
    unsigned char address[6];
    char data[32];
    int index = 0;

  public:
    MyNRF(char _address[]) : radio(CE, CSN) {
      for (int i = 0; i < 6; i++) {
        address[i] = _address[i];
      }
    };

    void init();
    void sendText(String text);
    void sendData(
      float temp, float humi,
      float co, float lpg, float smoke,
      double lat, double lng
      );
    void sendImage();
};

void MyNRF::init() {
  // Initialize the transceiver on the SPI bus
  if (!radio.begin()) {
    Serial.println(F("[MyNRF]: Radio hardware is not responding!!"));
    // Hold in infinite loop
    while (1);
  }

  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MAX);
  radio.setDataRate(RF24_2MBPS);
  radio.stopListening();

  Serial.println(F("[MyNRF]: Setup finished"));
}


void MyNRF::sendText(String text) {
  radio.write(text.c_str(), text.length());

  String res = "[NRF]: (send_text) " + text;
  Serial.write(res.c_str());
}

// temp=1000&humi=1000
// co=10000&lpg=10000&smoke=1000
// lat=123.123456&lng=123.123456
// !
void MyNRF::sendData(
  float temp, float humi,
  float co, float lpg, float smoke,
  double lat, double lng
) {
  String dhtxStr = "temp=" + String(temp) + "&humi=" + String(humi) + "&";
  String mqxStr = "co=" + String(co) + "&lpg=" + String(lpg) + "&smoke=" + String(smoke) + "&";
  String locationStr = "lat=" + String(lat) + "&lng=" + String(lng);

  radio.write(dhtxStr.c_str(), dhtxStr.length());
  radio.write(mqxStr.c_str(), mqxStr.length());
  radio.write(locationStr.c_str(), locationStr.length());
  radio.write("!\r\n", 3);

  // String newData = "[NRF]: (send_data) " + dhtxStr + mqxStr + locationStr + "!\r\n";
  // Serial.println(newData);
}

void MyNRF::sendImage() {
  log("Read and Send image");

  while (1) {
    if (Serial.available()) {
      char c = Serial.read();
      data[index] = c;

      // Check if found '!' in current index then send the rest data and break from the while loop
      if (data[index] == '!') {
        radio.write(&data, index);

        // Clear data and index
        char data[32];
        index = 0;

        // Break from the while loop
        break;
      }

      index++;
      // Send data every 32 bytes and clear data buffer
      if (index == 32) {
        radio.write(&data, 32);

        // Clear data and index
        char data[32];
        index = 0;
      }
    }
  }
}

MyNRF myNrf("101001");
