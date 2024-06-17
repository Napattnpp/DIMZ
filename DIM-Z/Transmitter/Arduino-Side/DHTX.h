class DHTX {
  public:
    float temperature = 0;
    float humidity = 0;
    DHT dht;

    DHTX() : dht(DHT_PIN, DHT_TYPE) {};

    void init();
    void get();
    void log();
};

void DHTX::init() {
  dht.begin();
}

void DHTX::get() {
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();
}

void DHTX::log() {
  Serial.print("\tTemperature (C)\t\t|\tHumidity (%)\n");
  Serial.print("\t" + String(temperature)  + "\t\t\t|\t" + String(humidity) + "\n");
  Serial.print("--------------------------------------------------------\n");
}

DHTX dhtx;
