/* Set a single Sensor address into EEPROM.
 * Write the value of its address into the payload as a list of 8 2-digit HEX values
 * Write the Sensor's index (0-80, counting along each row from the corner where the 
 * wires are) into the sensorID field. Then run once on the arduino.
 * MAKE SURE to re-upload the single_sensor_bus program after running this one.
*/

#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>

DeviceAddress payload = {0x28, 0xC6, 0x43, 0x8A, 0x0E, 0x00, 0x00, 0xA2};
int sensorID = 80;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  EEPROM.put(sensorID * 8, payload);
  Serial.println("placed");
  DeviceAddress value;
  printAddress(EEPROM.get(sensorID*8, value));  
  while(true){}
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
