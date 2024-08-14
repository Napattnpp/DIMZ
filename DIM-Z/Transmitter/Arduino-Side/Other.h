void log(String toLog) {
  Serial.print(TAG);
  Serial.println(toLog);
}

// Send message and Waiting for ...
void SAW(String toSend, String toWaitingFor) {
  Serial.print(toSend);
  while (Serial.readString() != toWaitingFor);
}