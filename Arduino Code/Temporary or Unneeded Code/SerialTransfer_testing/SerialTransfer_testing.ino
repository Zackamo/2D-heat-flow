#include "SerialTransfer.h"

SerialTransfer myTransfer;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //myTransfer.begin(Serial);
}

void loop() {
  // put your main code here, to run repeatedly:
  double myList[] = {32, 567.8, 256724.4, 23456, 2.235, 245.666};
  //myTransfer.sendDatum(myList);
  Serial.print("hi!|");
  delay(1000);
}
