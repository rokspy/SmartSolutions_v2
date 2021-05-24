#include <IRremote.h>


IRsend transmit_data;

int serial_read;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Turn off the LED (depends on how connection to relay is made)
  if(Serial.available()){
    serial_read = Serial.read();
    if(serial_read == 48){          // Use "No line ending" in serial monitor
        transmit_data.sendNEC(0xFF6897, 32);
        transmit_data.sendNEC(0xFF6897, 32);
        transmit_data.sendNEC(0xFF6897, 32);
    }
    // Turn ON the LED (depends on how connection to relay is made)
    else if(serial_read == 49){     // Use "No line ending" in serial monitor
        transmit_data.sendNEC(0xFF30CF, 32);
        transmit_data.sendNEC(0xFF30CF, 32);
        transmit_data.sendNEC(0xFF30CF, 32);
    }
  }
}
