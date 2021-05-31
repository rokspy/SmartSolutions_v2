#include <SoftwareSerial.h>

SoftwareSerial mySer(3,4);

void setup() {
  mySer.begin(9600);
  Serial.begin(9600);

}

void loop() {
  if(Serial.available()){
    mySer.print(Serial.readString());
  }
  if(mySer.available()){
    Serial.println(mySer.readString());
  }
}
