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

DeviceAddress address;
DeviceAddress value;
int mem_pos = 0;
bool done;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");
  sensors.begin();
  done = false;
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(" Requesting Temperatures. . .");
  sensors.requestTemperatures();
  Serial.println("Done");
  Serial.print("Temperature is: "); 
  Serial.println(sensors.getTempCByIndex(0));
  sensors.getAddress(address,0);
  printAddress(address);
  Serial.println(sizeof(address));
  if(!done){
    EEPROM.put(8 * mem_pos, address);
  }
  delay(1000);
  EEPROM.get(8 * mem_pos, value);
  printAddress(value);
  if(sensors.validAddress(value)){
    Serial.println("yay!");
    done = true;
  }
  else{
    Serial.println("uh oh!");  
  }
}

// function to print a device address
void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    // zero pad the address if necessary
    if (deviceAddress[i] < 16) Serial.print("0");
    Serial.print(deviceAddress[i], HEX);
  }
  Serial.println("");
}
