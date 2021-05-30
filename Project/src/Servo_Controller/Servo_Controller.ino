#include<Servo.h>

Servo camera_servo;
int servo_pos = 90;

void setup() {
  // put your setup code here, to run once:
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  camera_servo.attach(4);
  Serial.begin(9600);
  camera_servo.write(90);
}

void loop() {
  if(digitalRead(5) && !digitalRead(6)){
    if(servo_pos != 180){
      servo_pos++;
    }
    Serial.print("Turning Right, servo pos: "); Serial.println(servo_pos);
    camera_servo.write(servo_pos);
    delay(50);
  }
  if(digitalRead(6) && !digitalRead(5)){
    if(servo_pos != 0){
      servo_pos--;
    }
    Serial.print("Turning Left, servo pos: "); Serial.println(servo_pos);
    camera_servo.write(servo_pos);
    delay(50);
  }
}
