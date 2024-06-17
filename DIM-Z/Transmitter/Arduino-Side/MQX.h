class MQX {
  private:
    MQ2 mq2;

  public:
    float co = 0.0;
    float lpg = 0.0;
    float smoke = 0.0;

    MQX() : mq2(MQX_PIN) {}

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

MQX mqx;
