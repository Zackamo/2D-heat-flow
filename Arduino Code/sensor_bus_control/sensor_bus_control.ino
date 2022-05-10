#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2 //set pin number used

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

#define NUM_SENSORS

DeviceAddress addresses[NUM_SENSORS];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");
  sensors.begin();
  DeviceAddress temp;
  for(int i = 0; i < NUM_SENSORS; i++){
    EEPROM.get(8*i, temp)
    if(sensors.validAddress(temp)){
      addresses[i] = temp;
    }
    else{
      Serial.print("Failed to Detect Sensor at Position: ");
      Serial.print(i);
      Serial.print(", Address: ");
      Serial.println(temp);
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
  address = 0;
  sensors.getAddress(address,0);
  Serial.print("Sensor Address: ");
  Serial.println(*address);
  delay(1000);

}
