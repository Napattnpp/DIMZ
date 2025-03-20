void onDetected(int key) {
  if (key == 0) {
    // Fire is detected
    myNrf.sendText("Fire is detected\r\n");
    myNrf.sendImage();

    /* [TODO]
       * Send (DHT, MQ, Location) to raspberry pi
       ! Read image from Raspberry pi
       ! Send image to Datacenter
      */
  } else if (key == 1) {
    // Smoke is detected
    myNrf.sendText("Smoke is detected\r\n");
    myNrf.sendImage();

    /* [TODO]
       * Send (DHT, MQ, Location) to raspberry pi
       ! Read image from Raspberry pi
       ! Send image to Datacenter
      */
  }
}