#include <SoftwareSerial.h>

SoftwareSerial mySer(3,4); // RX,TX

// Arduino UNO ADC resolution = 10bit (1023)

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

float analogConvert(int analog_pin);

void loop() {
  Serial.println(analogConvert(A0));
  delay(1000);

}

float analogConvert(int analog_pin){
  return analogRead(analog_pin)/1023.0 * 5.0;
}
