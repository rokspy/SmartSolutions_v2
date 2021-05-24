#include <IRremote.h>

int LED = 13;
int IR_RX = 11;

IRrecv irrecv(IR_RX);
decode_results received_data;

long int data;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
  irrecv.enableIRIn();
}

void loop() {
  if (irrecv.decode(&received_data)) {
    if(received_data.value == 0xFF6897){
      digitalWrite(LED,LOW);         
    }
    else if (received_data.value == 0xFF30CF){
      digitalWrite(LED,HIGH);           
    }
    Serial.println(received_data.value, HEX); 
    irrecv.resume();
  }
}
