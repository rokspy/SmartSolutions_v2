/*  Accesspoint - station communication without router
 *  see: https://github.com/esp8266/Arduino/blob/master/doc/esp8266wifi/station-class.rst
 *  Works with: accesspoint_bare_01.ino
 */

/* 
 * Code partly taken from:
 * http://www.esp8266learning.com/the-wemos-pir-shield.php
 */

#include <ESP8266WiFi.h>

//LM35 stuff
int val;
int tmpPin=0;
float mv,cel;

const int PIR = D2;
int PIR_state = 0;

byte ledPin = 2;
char ssid[] = "rokspy_AP";           // SSID of your AP
char pass[] = "Wemos_comm";         // password of your AP

IPAddress server(10,10,10,1);     // IP address of the AP
WiFiClient client;

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, pass);           // connects to the WiFi AP
  Serial.println();
  Serial.println("Connection to the AP");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.println("Connected");
  Serial.print("LocalIP:"); Serial.println(WiFi.localIP());
  Serial.println("MAC:" + WiFi.macAddress());
  Serial.print("Gateway:"); Serial.println(WiFi.gatewayIP());
  Serial.print("AP MAC:"); Serial.println(WiFi.BSSIDstr());
  pinMode(ledPin, OUTPUT);

  pinMode(PIR, INPUT);
}

void loop() {

  PIR_state = digitalRead(PIR);
  
  if(PIR_state == HIGH){
    Serial.println("Someone Detected");
    if(client.connect(server, 80) == 1){
      digitalWrite(ledPin, LOW);
      client.println("1\r");
      client.flush();
      digitalWrite(ledPin, HIGH);
      client.stop();
      delay(5000);
    }
    else Serial.println("Couldn't establish a connection");
  }
  else Serial.println("Nothing Detected");
  delay(100);
}
