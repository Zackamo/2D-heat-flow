/* single_sensor_test.ino
 * By: Zack Johnson, Osip Surdutovich, Kanisk Pandey
 * 
 * Simple program to read the temperature and address from a single DS18B20 Sensor.
 * This program can be used to test the operation of the sensors as well as to determine 
 * their addresses for sensor locating.
*/

#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2 //set pin number used

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");
  sensors.begin();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(" Requesting Temperatures. . .");
  sensors.requestTemperatures();
  Serial.println("Done");
  Serial.print("Temperature is: "); 
  Serial.print(sensors.getTempCByIndex(0));
  uint8_t* address = 0;
  sensors.getAddress(address,0);
  Serial.print("Sensor Address: ");
  Serial.println(*address);
  delay(1000);

}
