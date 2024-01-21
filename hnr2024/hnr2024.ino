/**
   BasicHTTPClient.ino

    Created on: 24.05.2015

*/

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Servo.h>
#include "pitches.h"

ESP8266WiFiMulti WiFiMulti;
Servo myservo; 
#define BUZZER 15

void setup() {
  myservo.attach(13);  // attaches the servo on pin 9 to the servo object
  myservo.write(180);  
  pinMode(BUZZER, OUTPUT);
  delay(5000);

  Serial.begin(115200);
  // Serial.setDebugOutput(true);

  Serial.println();
  Serial.println();
  Serial.println();

  for (uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }

  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP("Hackerspot", "hacking101");
}

void loop() {
  // wait for WiFi connection
  if ((WiFiMulti.run() == WL_CONNECTED)) {

    WiFiClient client;

    HTTPClient http;

    Serial.print("[HTTP] begin...\n");
    if (http.begin(client, "http://192.168.60.124:8000/counter/")) {  // HTTP


      Serial.print("[HTTP] GET...\n");
      // start connection and send HTTP header
      int httpCode = http.GET();

      // httpCode will be negative on error
      if (httpCode > 0) {
        // HTTP header has been send and Server response header has been handled
        Serial.printf("[HTTP] GET... code: %d\n", httpCode);
        
        // file found at server
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          Serial.println("[HTTP] GET - output");
          String payload = http.getString();
          Serial.println(payload);
          Serial.println("HTTP GET - output end");
          attack();
        }
      } else {
        Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }

      http.end();
    } else {
      Serial.println("[HTTP] Unable to connect");
    }
  }

  delay(1000);
}

void attack(){
  Serial.println("attack");
  //tone(BUZZER, NOTE_C5, 20);
  digitalWrite(BUZZER, 1);
  myservo.write(0);  
  delay(1000);
  myservo.write(180);  
  digitalWrite(BUZZER, 0);
  delay(5000);
}