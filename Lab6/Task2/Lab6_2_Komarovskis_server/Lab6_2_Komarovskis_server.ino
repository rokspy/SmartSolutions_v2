/*  Accesspoint - station communication without router
 *  see: https://github.com/esp8266/Arduino/blob/master/doc/esp8266wifi/soft-access-point-class.rst
 *       https://github.com/esp8266/Arduino/blob/master/doc/esp8266wifi/soft-access-point-examples.rst
 *       https://github.com/esp8266/Arduino/issues/504
 *  Works with: station_bare_01.ino
 */ 


#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>

WiFiServer server(80);
IPAddress IP(10,10,10,1);
IPAddress mask = (255, 255, 255, 0);

SoftwareSerial mySer(D1,D2);

byte ledPin = 2;

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_AP_STA);
  WiFi.softAPConfig(IP, IP, mask);
  WiFi.softAP("rokspy_AP", "Wemos_comm");
  server.begin();
  pinMode(ledPin, OUTPUT);
  Serial.println();
  Serial.println("accesspoint_bare_01.ino");
  Serial.println("Server started.");
  Serial.print("IP: ");     Serial.println(WiFi.softAPIP());
  Serial.print("MAC:");     Serial.println(WiFi.softAPmacAddress());
  mySer.begin(9600);
}

void loop() {
  WiFiClient client = server.available();
  if (!client) {return;}
  digitalWrite(ledPin, LOW);
  if(client.available()){
    String request = client.readStringUntil('\r');
    Serial.println("********************************");
    Serial.println("From the station " + request);
    mySer.print(request);
    client.flush();
  }
//  Serial.print("Byte sent to the station: ");
//  Serial.println(client.println(request + "ca" + "\r"));
  String saadetud=Serial.readString();
  client.println(saadetud+"\r");
//  Serial.println(saadetud);
  digitalWrite(ledPin, HIGH);
}
