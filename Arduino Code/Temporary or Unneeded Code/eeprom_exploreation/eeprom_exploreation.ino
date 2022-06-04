#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>

void setup() {
  // put your setup code here, to run once:
  int registers[10][10];
  Serial.begin(9600);
  //arduino uno has eeprom addresses 0-511 (each 1 byte)
  
}

void loop() {
  // put your main code here, to run repeatedly:
  byte value;
  value = EEPROM.read(10);
  Serial.println(value);
  if(value != 42){
    EEPROM.write(10,42);
  }
  delay(1000);
}
