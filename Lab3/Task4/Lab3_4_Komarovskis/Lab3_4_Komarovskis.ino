#include <SoftwareSerial.h>

SoftwareSerial mySer(3,4); // RX,TX

// Arduino UNO ADC resolution = 10bit (1023)

int temp;

void setup() {
  Serial.begin(9600);
  mySer.begin(9600);
  pinMode(A3, INPUT);
}

float analogConvert(int analog_pin);

void loop() {
  temp = analogConvert(A3) * 1000;
  Serial.println(temp);
  mySer.print(temp);
  delay(1000);

}

float analogConvert(int analog_pin){
  return analogRead(analog_pin)/1023.0 * 5.0;
}
