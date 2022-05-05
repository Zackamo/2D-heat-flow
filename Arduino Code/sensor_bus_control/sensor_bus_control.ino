#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2 //set pin number used

OneWire onewire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  // put your setup code here, to run once:
  int registers[10][10];
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");
  sensors.begin();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(" Requesting Temperatures. . .");
  sensors.requestTemperatures();
  Serial println("Done");
  Serial.print("Temperature is: "); 
  Serial.print(sensors.getTempCByIndex(0));
  delay(1000);

}
