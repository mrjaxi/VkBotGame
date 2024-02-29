#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <LiquidCrystal_I2C.h>

#include <SPI.h>
#include <MFRC522.h>


#define RST_PIN D3
#define SS_PIN D4

//#define ledpin 1

WiFiClient wifiClient;
LiquidCrystal_I2C lcd(0x27, 16, 2);

const String position_ = "9";

//const String ssid = "YOTA-7EAD";
// 
//const String password = "50007900";
 
//const String ssid = "YOTA-5647-2.4GHz";
 
//const String password = "67411435";

MFRC522 mfrc522(SS_PIN, RST_PIN);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //pinMode(ledpin, OUTPUT);
  SPI.begin();
  mfrc522.PCD_Init();

  WiFi.begin(ssid, password);
  Serial.println("Connecting"); 
  while(WiFi.status() != WL_CONNECTED) { 
    delay(500); 
    Serial.print(".");
  }
   
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");   
  Serial.println(WiFi.localIP());

  
  //lcd.begin(16,2);
  lcd.init();
  lcd.backlight();
}

void loop() {

  if(mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()){
      //Проверяем соединение WiFi 
      if(WiFi.status()== WL_CONNECTED){
          HTTPClient http;
          // Укажите URL или IP вашего домена
          http.begin(wifiClient, "http://u1946154.isp.regruhosting.ru/post-data.php");
          // Указываем тип данных
          http.addHeader("Content-Type", "application/x-www-form-urlencoded"); 
          String uid_;
          Serial.println();
          uid_+=String(mfrc522.uid.uidByte[1])+String(mfrc522.uid.uidByte[2])+String(mfrc522.uid.uidByte[3]);
          Serial.print(F("Card UID: "));
          Serial.println(uid_.toInt());
          
          // Подготавливаем запрос   
          String httpRequestData ="cardid=" + String(uid_.toInt()) + "&position=" + position_;
        
          Serial.print("httpRequestData: ");
          Serial.println(httpRequestData);
          // Отправляем запрос
          //int httpResponseCode = http.POST("cardid=111&position=100");
          int httpResponseCode = http.POST(httpRequestData);
          if (httpResponseCode>0) {
              //digitalWrite(ledpin, HIGH);
              Serial.print("HTTP Response code: ");  
              Serial.println(httpResponseCode);
              lcd.setCursor(5, 0);
              // Print HELLO to the screen, starting at 5,0.
              lcd.print("Your ID");
              // Move the cursor to the next line and print
              lcd.setCursor(4, 1);      
              lcd.print(uid_);
          }
          else {
              Serial.print("Error code: "); 
              Serial.println(httpResponseCode);
          }
          // Освобождаем память
          http.end();
        
      }else{
          Serial.println("WiFi Disconnected");
      }
      delay(2000);
      lcd.setCursor(1, 0);
      // Print HELLO to the screen, starting at 5,0.
      lcd.print("    ATTACH  ");
      // Move the cursor to the next line and print
      lcd.setCursor(1, 1);      
      lcd.print("     NFC     ");
     // digitalWrite(ledpin, LOW);
  }


  
}