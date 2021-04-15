#include <SoftwareSerial.h>
#include <DallasTemperature.h>
#include <OneWire.h>

// LAB3 => 2.3.2.

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensor(&oneWire);

int rec;

SoftwareSerial mySer(3,4); // RX TX

void setup(){
  Serial.begin(9600);
  while(!Serial){
    ;
  }
  mySer.begin(9600);
  sensor.begin();
}

void loop() // run over and over
{
  if(mySer.available()){
    rec = mySer.read(); 
  }
  if(rec == 57){
    sensor.requestTemperatures();
    mySer.print(sensor.getTempCByIndex(0));
    rec = 0;
  }
}
