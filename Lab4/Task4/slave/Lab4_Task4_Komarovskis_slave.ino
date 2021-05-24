
#include <SoftwareSerial.h>
#include <DallasTemperature.h>

SoftwareSerial bt(2,3); // rx,tx

#define ONE_WIRE_BUS 4

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensor(&oneWire);



int VCCpin=13;

String slaveName="rokspy_slave";

String rec;

int counter=0;
String inputString,outputString;

void setup() {

  sensor.begin();
  
  pinMode(VCCpin, OUTPUT);
  digitalWrite(VCCpin, HIGH);
  bt.begin(9600);
  Serial.begin(9600);
  delay(1000);
  bt.print("AT+NAME:rokspy_slave\r\n");
  bt.print("AT+NAME?\n\r");
  delay(100);
  bt.print("AT+PSWD:1234\r\n");
  bt.print("AT+PSWD?\r\n");
}

void loop(){
  if(bt.available()){
    rec = bt.readString();
    if(rec == "send"){
      sensor.requestTemperatures();
      bt.print(sensor.getTempCByIndex(0));
    }
  }
  //Serial.println(sensor.getTempCByIndex(0));

}
