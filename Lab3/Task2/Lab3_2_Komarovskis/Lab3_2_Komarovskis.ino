#include <SoftwareSerial.h>

SoftwareSerial mySer(3,4) // RX,TX
int read_data;


void setup() {
  Serial.begin(9600);
  mySer.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if(mySer.available()){
    read_data = mySer.read();
    if(read_data == 0)        digitalWrite(13, LOW);
    else if(read_data == 1)   digitalWrite(13, HIGH);
    else                      mySer.write(digitalRead(13));
  }
}
