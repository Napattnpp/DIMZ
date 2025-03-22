class MQX {
  private:
    MQ2 mq2;

  public:
    float co = 0.0;
    float lpg = 0.0;
    float smoke = 0.0;

    MQX(int _mqx_pin) : mq2(_mqx_pin) {}

    void init();
    void get();
    void log();
};

void MQX::init() {
  mq2.begin();
}

void MQX::get() {
  co = mq2.readCO();
  lpg = mq2.readLPG();
  smoke = mq2.readSmoke();
}

void MQX::log() {
  Serial.print("\tCO \t|\tLPG \t|\tSmoke \n");
  Serial.print("\t" + String(co)  + "\t|\t" + String(lpg) + "\t|\t" + String(smoke) + "\n");
  Serial.print("--------------------------------------------------------\n");
}
