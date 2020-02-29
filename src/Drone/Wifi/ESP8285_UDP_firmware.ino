#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

#ifndef STASSID
#define STASSID "OnePlus" 
#define STAPSK  "zombie@11"
#endif

IPAddress staticIP(192, 168, 43, 4); //ESP static ip
IPAddress gateway(192, 168, 43, 1);   //IP Address of your WiFi Router (Gateway)
IPAddress subnet(255, 255, 255, 0);  //Subnet mask
IPAddress dns(8, 8, 8, 8);  //DNS

unsigned int localPort = 8888;      // local port to listen on

char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1]; //buffer to hold incoming packet,
char cmdBuffer[UDP_TX_PACKET_MAX_SIZE + 1];   //buffer to hold incoming packet,
// unsigned int packetLength = 0;
unsigned int cmdLength = 0;
bool flag = false;
WiFiUDP Udp;

// unsigned long lastrx = millis();

void setup() {
  
    Serial.begin(115200);
    Serial1.begin(115200);
    WiFi.mode(WIFI_STA);
    WiFi.config(staticIP, gateway, subnet);
    WiFi.begin(STASSID, STAPSK);
    while (WiFi.status() != WL_CONNECTED){
        delay(500);
      }
    Serial1.print('connected');
    
    ArduinoOTA.setPort(8266);
    ArduinoOTA.setPasswordHash("fa86b8f1bf7e8b9a6cb4fa77d54159a1");
    ArduinoOTA.onStart([]() {
    String type;
    if (ArduinoOTA.getCommand() == U_FLASH)
        type = "sketch";
    else // U_SPIFFS
        type = "filesystem";

    // NOTE: if updating SPIFFS this would be the place to unmount SPIFFS using SPIFFS.end()
    Serial1.println("Start updating " + type);
    });
    ArduinoOTA.onEnd([]() {
        Serial1.println("\nEnd");
    });
    ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
        Serial1.printf("Progress: %u%%\r", (progress / (total / 100)));
    });
    ArduinoOTA.onError([](ota_error_t error) {
        Serial1.printf("Error[%u]: ", error);
        if (error == OTA_AUTH_ERROR) Serial1.println("Auth Failed");
        else if (error == OTA_BEGIN_ERROR) Serial1.println("Begin Failed");
        else if (error == OTA_CONNECT_ERROR) Serial1.println("Connect Failed");
        else if (error == OTA_RECEIVE_ERROR) Serial1.println("Receive Failed");
        else if (error == OTA_END_ERROR) Serial1.println("End Failed");
    });
    ArduinoOTA.begin();
    
    Serial1.print("Connected! IP address: ");
    Serial1.println(WiFi.localIP());
    Serial1.printf("UDP server on port %d\n", localPort);
    Udp.begin(localPort);
}

void loop() {
    
    ArduinoOTA.handle();

    int packetSize = Udp.parsePacket();
    
    if(packetSize) {
        Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
        unsigned int packetLength = packetSize;
        Serial1.print("packet recieved");
        Serial1.println(packetBuffer);
        if(packetLength == 6)
        {
            byte rxBuffer[12];
            uint8_t rxBufLen = 0;
            Serial.write((byte*)packetBuffer, 6);
           // delay(1);
            while (Serial.available())
            {
                rxBuffer[rxBufLen] = Serial.read();
                rxBufLen++;
            }
            Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
            Udp.write((byte*)rxBuffer, rxBufLen+1);
            Udp.endPacket();
        }
        if(packetLength == 22)
        {
            memcpy(cmdBuffer, packetBuffer, packetLength);
            cmdLength = packetLength;
            flag  = true;
        }
        memset(packetBuffer, 0, packetLength);
        packetLength = 0;
        //lastrx = millis();
        delay(100);
    }
    
    // if ((millis() - lastrx < 1000) && flag == true)
    if (flag == true)
    {
        Serial.write((byte*)cmdBuffer, cmdLength);
        delay(100);
    }
//    else if (millis() - lastrx > 1500 && flag == true)
//    {
//        Serial1.println("timeout");
//        uint8_t data[16] = {220, 5, 220, 5, 232, 3, 220, 5, 232, 3, 0, 0, 0, 0, 0, 0};
//        failMode(200, data, 16);
//        memset(cmdBuffer, 0, cmdLength);
//        cmdLength = 0;
//        delay(200);
//    }
}
//
//void failMode(uint8_t cmd, uint8_t *data, uint8_t n_bytes) {
//
//    char *str = "$M<";
//    uint8_t checksum = 0;
//    checksum ^= n_bytes;
//      
//    checksum ^= cmd;
//
//    *(str + 3) = n_bytes;
//    *(str + 4) = cmd;
//
//    for (int i = 0 ; i < 16; i++)
//    {
//        *(str+5+i) = data[i];
//        checksum ^=  data[i];
//    }
//
//    *(str + 21) = checksum;
//    Serial.write((byte*)str,22);
//
//    strcpy((char*)cmdBuffer, str);
//    //memcpy(cmdBuffer, packetBuffer, packetLength)
//}
