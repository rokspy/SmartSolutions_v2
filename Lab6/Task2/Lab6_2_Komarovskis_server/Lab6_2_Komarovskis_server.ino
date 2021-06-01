/*  Accesspoint - station communication without router
 *  see: https://github.com/esp8266/Arduino/blob/master/doc/esp8266wifi/soft-access-point-class.rst
 *       https://github.com/esp8266/Arduino/blob/master/doc/esp8266wifi/soft-access-point-examples.rst
 *       https://github.com/esp8266/Arduino/issues/504
 *  Works with: station_bare_01.ino
 */ 


#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>
WiFiServer server(80);
WiFiServer server_for_LED(81);
IPAddress IP(10,10,10,1);
IPAddress mask = (255, 255, 255, 0);

byte ledPin = 2;

unsigned long measure_time;

bool timer = 0;
bool sonar_state = 0;

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_AP_STA);
  WiFi.softAPConfig(IP, IP, mask);
  WiFi.softAP("rokspy_AP", "Wemos_comm");
  server.begin();
  server_for_LED.begin();
  pinMode(ledPin, OUTPUT);
  Serial.println();
  Serial.println("accesspoint_bare_01.ino");
  Serial.println("Server started.");
  Serial.print("IP: ");     Serial.println(WiFi.softAPIP());
  Serial.print("MAC:");     Serial.println(WiFi.softAPmacAddress());
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    digitalWrite(ledPin, LOW);
    if(client.available()){
      String request = client.readStringUntil('\r');
      client.flush();
      Serial.println("********************************");
      Serial.println("From the station " + request);

      // If receives signal from PIR, starts timer, enables the led 
      if(request == '1'){
        WiFiClient client = server_for_LED.available();
        if (client) {
          measure_time = millis();
          timer = 1;
          sonar_state = 0;
          // Enable the LED
          // ...
        }
      }
      else if(request == '2'){
        sonar_state ^= 1;
        if(!timer){
          // Send LED state to the client. Sonar state determines the LED state
          // ... 
        }
      }
    }
  }
  // If timer is on then waits till it turns off set the appropriate led state
  if(millis() - measure_time > 30000){ 
    timer = 0;
    // Send LED state to the client. Sonar state determines the LED state
  }
  digitalWrite(ledPin, HIGH);
}
