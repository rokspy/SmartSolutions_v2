/*  Accesspoint - station communication without router
 *  see: https://github.com/esp8266/Arduino/blob/master/doc/esp8266wifi/station-class.rst
 *  Works with: accesspoint_bare_01.ino
 */

#include <ESP8266WiFi.h>

//LM35 stuff
int val;
int tmpPin=0;
float mv,cel;

byte ledPin = 2;
char ssid[] = "robootika";           // SSID of your AP
char pass[] = "DigiLaboriArvutiKlass";         // password of your AP

IPAddress server(172,17,54,208);     // IP address of the AP
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
  Serial.println("station_bare_01.ino");
  Serial.print("LocalIP:"); Serial.println(WiFi.localIP());
  Serial.println("MAC:" + WiFi.macAddress());
  Serial.print("Gateway:"); Serial.println(WiFi.gatewayIP());
  Serial.print("AP MAC:"); Serial.println(WiFi.BSSIDstr());
  pinMode(ledPin, OUTPUT);
}

void loop() {
  client.connect(server, 8888);
  digitalWrite(ledPin, LOW);
  Serial.println("********************************");
  Serial.print("Byte sent to the AP: ");
//  Serial.println(client.print("Anyo\r"));
//  String saadetud=Serial.readString();
//  client.println(saadetud+"\r");
//  Serial.println(saadetud);
  val = analogRead(tmpPin);
  Serial.print(val);
  Serial.print(" ");
  mv=val*3300/1024;
  Serial.print(" ");
  Serial.print(mv);
  Serial.print("  ");
  cel=mv/10;
  
  Serial.print("Temp: ");
  Serial.print(cel);
  Serial.println("*C");
  client.println(String(cel)+"\r");
  String answer = client.readStringUntil('\r');
  Serial.println("From the AP: " + answer);
  client.flush();
  digitalWrite(ledPin, HIGH);
  client.stop();
  delay(2000);
}
