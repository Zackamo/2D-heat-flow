#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <SerialTransfer.h>

#define NUM_SENSORS 81
#define ONE_WIRE_BUS 2 //set pin number used

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);


double measurement_rate = 1; //Time between measurements in seconds
DeviceAddress address_list[NUM_SENSORS];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sensors.begin();
  DeviceAddress tempAdr;
  for(int i = 0; i < NUM_SENSORS; i++){
    EEPROM.get(8*i, tempAdr);
    if(sensors.validAddress(tempAdr)){
      memcpy(address_list[i], tempAdr, sizeof(DeviceAddress));
      Serial.print("Detected Sensor at Position: ");
      Serial.print(i);
      Serial.print(", Address: ");
      printAddress(tempAdr);
      Serial.println("|");
    }
    else{
      Serial.print("Failed to Detect Sensor at Position: ");
      Serial.print(i);
      Serial.print(", Address: ");
      printAddress(tempAdr);
      Serial.println("|");
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  sensors.requestTemperatures();
  
  for (int i = 0; i < 9; i++){
    for (int j = 0; j < 9; j++){
      int location = (i*9)+j;
      float temperature = sensors.getTempC(address_list[0]);
      String packet = String("&");
      packet += i;
      packet += ",";
      packet += j;
      packet += ",";
      packet += temperature;
      packet += "|";
      Serial.println(packet);
    }
  }
  Serial.println("End of timestep|");
  delay(1000 * measurement_rate);
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
}
