#include <EEPROM.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define NUM_SENSORS 81
#define ONE_WIRE_BUS 2 //set pin number used

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);


double measurement_rate = 1; //Time between measurements in seconds
DeviceAddress address_list[NUM_SENSORS];
DeviceAddress currentAddr;
unsigned long delay_time = measurement_rate * 1000;
unsigned long last_measurement = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sensors.begin();
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

void loop() {
  // put your main code here, to run repeatedly:
  if(millis()- last_measurement >= delay_time){
    last_measurement = millis();
    sensors.requestTemperatures();
    int EAddress = 0;
    for (int n = 0; n < NUM_SENSORS; n++){
        for(byte b = 0; b < 8; b++){
            currentAddr[b] = EEPROM.read(EAddress);
            EAddress += 1;
        }
        int i = n / 9;
        int j = n % 9;
        printAddress(currentAddr);
        float temperature = sensors.getTempC(currentAddr);
        Serial.println(temperature);
        String packet = String("&");
        packet += i;
        packet += ",";
        packet += j;
        packet += ",";
        packet += temperature;
        packet += "|";
        Serial.println(packet);
      }
    Serial.println("End of timestep|");
  }
}
