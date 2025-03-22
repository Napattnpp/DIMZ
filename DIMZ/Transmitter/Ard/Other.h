// Send message and Waiting for ...
void SAW(String toSend, String toWaitingFor) {
  String data;
  
  unsigned long ct = 0;
  unsigned long pt = 0;

  Serial.print(toSend);
  while (1) {
    data = Serial.readString();

    if (data == toWaitingFor) {
      break;
    }

    ct = millis();

    if (ct-pt >= 3000) {
      Serial.print(toSend);

      pt = ct;
    }
  }

  Serial.print(data);
}