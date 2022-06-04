#include <OneWire.h>
#include <DallasTemperature.h>
#include <EEPROM.h>

#define NUM_SENSORS 81
#define ONE_WIRE_BUS 2 //set pin number used

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

DeviceAddress SAddress;
DeviceAddress realAddress;

// function to print a device address
void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    // zero pad the address if necessary
    if (deviceAddress[i] < 16) Serial.print("0");
    Serial.print(deviceAddress[i], HEX);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sensors.begin();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  sensors.requestTemperatures();
  for (byte i = 0; i < 8; i++){
      SAddress[i] = EEPROM.read(i);
  }
  Serial.println("EEPROM test");
  Serial.println(SAddress[1], HEX);
  printAddress(SAddress);
  Serial.println(sensors.getTempC(SAddress));
  sensors.getAddress(realAddress, 0);
  Serial.println("Read Sensor test");
  printAddress(realAddress);
  Serial.println(sensors.getTempC(realAddress));
  Serial.println("Hard Coded");
  DeviceAddress temp = {0x28, 0xF0, 0xEC, 0x8A, 0x0E, 0x00, 0x00, 0xA1};
  Serial.println(sensors.getTempC(temp));
  while(true){} 
}
