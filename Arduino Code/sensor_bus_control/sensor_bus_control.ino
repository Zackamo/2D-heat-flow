#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <SerialTransfer.h>

#define ONE_WIRE_BUS 2 //set pin number used

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

#define NUM_SENSORS 81

DeviceAddress address_list[NUM_SENSORS];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");
  sensors.begin();
  DeviceAddress tempAdr;
  for(int i = 0; i < NUM_SENSORS; i++){
    EEPROM.get(8*i, tempAdr);
    if(sensors.validAddress(tempAdr)){
      memcpy(address_list[i], tempAdr, sizeof(DeviceAddress));
    }
    else{
      Serial.print("Failed to Detect Sensor at Position: ");
      Serial.print(i);
      Serial.print(", Address: ");
      printAddress(tempAdr);
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(" Requesting Temperatures. . .");
  sensors.requestTemperatures();
  Serial.println("Done");
  Serial.print("Temperature is: "); 
  Serial.print(sensors.getTempCByIndex(0));
  delay(1000);

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
