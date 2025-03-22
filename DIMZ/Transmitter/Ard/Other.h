String data;
  
unsigned long ct = 0;
unsigned long pt = 0;

// Send message and Waiting for ...
bool SAW(String toSend, String toWaitingFor) {

  // Check if toWaitingFor is received
  if (Serial.available() > 0) {
    data = Serial.readString();

    Serial.print(data);
    if (data == toWaitingFor) return true;
  }

  // Always send message every 3 second
  ct = millis();
  if (ct-pt >= 3000) {
    Serial.print(toSend);
    pt = ct;
  }

  return false;
}