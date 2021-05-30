/*  Accesspoint - station communication without router
 *  see: https://github.com/esp8266/Arduino/blob/master/doc/esp8266wifi/station-class.rst
 *  Works with: accesspoint_bare_01.ino
 */

/* 
 * Code partly taken from:
 * http://www.esp8266learning.com/wemos-mini-hc-sr04-ultrasonic-sensor.php
 */

#include <ESP8266WiFi.h>

#define echoPin D7 // Echo Pin
#define trigPin D6 // Trigger Pin

long distance, duration;

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
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

 void loop() {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    //Calculate the distance (in cm) based on the speed of sound.
    distance = duration/58.2;

    if(distance < 50){
      digitalWrite(ledPin, LOW);
      Serial.print("Value "); Serial.println(distance);
      client.println("2\r");
      client.flush();
      digitalWrite(ledPin, HIGH);
      client.stop();
      delay(5000);
    }

}
