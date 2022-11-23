#include <SoftwareSerial.h>
#include <Stepper.h>
#include <Wire.h>
#include "HX711.h"

const int stepsPerRevolution = 500;

Stepper beltStepper(stepsPerRevolution, 31, 33, 35, 37);

SoftwareSerial mySerial(10, 11);

float calibration_factor = 206275.00; 
#define zero_factor 8119092
#define DOUT  A3
#define CLK   A2
#define DEC_POINT  2

float offset = 0;
float get_units_kg();

HX711 scale(DOUT, CLK);

bool Send;
String sendTextSet = "Z0";
String Text;
String sendText;
int IR1 = 6;
int ValIR1 = 0;
bool wait1 = false;
int IR2 = 7;
int ValIR2 = 0;
bool wait2 = false;
unsigned long currentTime = millis();
int ScanerPin = 9;
String dataSection;
String dataRack;
String dataProductCode;
String dataQuantity;
String dataWeight;
String dataQRTimestamp;

unsigned long previousTime = millis();
long timeInterval = 1000;

void setup() {
  beltStepper.setSpeed(60);
  pinMode(IR1, INPUT);
  pinMode(IR2, INPUT);
  pinMode(31, OUTPUT);
  pinMode(33, OUTPUT);
  pinMode(35, OUTPUT);
  pinMode(37, OUTPUT);
  pinMode(ScanerPin, OUTPUT);
  Wire.begin(8);
  Wire.onRequest(requestEvent);
  Serial.begin(9600);
  mySerial.begin(9600);
  scale.set_scale(calibration_factor); 
  scale.set_offset(zero_factor);
  
}

void loop() {
  unsigned long currentTime = millis();
  checkIR1();
  ValIR2 = digitalRead(IR2);
  if (ValIR2 == 1) {
    clockwise();
  }
  if(currentTime - previousTime > timeInterval) {
    previousTime = currentTime;
    if (ValIR2 == 0) {
      digitalWrite(9, HIGH);
      delay(500);
      digitalWrite(9, LOW);
      delay(800);
      clockwise();
    }
  }    
  if (mySerial.available()) {
    String Text = mySerial.readString();
    Serial.print(Text);
    Serial.flush();
    String sendText = Text.substring(3, 5);
    if (sendText == "A1"){
      sendTextSet = "A1";
    } else if (sendText == "A2"){
      sendTextSet = "A2";
    } else if (sendText == "A3"){
      sendTextSet = "A3";
    } else if (sendText == "B1"){
      sendTextSet = "B1";
    } else if (sendText == "B2"){
      sendTextSet = "B2";
    } else if (sendText == "B3"){
      sendTextSet = "B3";
    } else if (sendText == "C1"){
      sendTextSet = "C1";
    } else if (sendText == "C2"){
      sendTextSet = "C2";
    } else if (sendText == "C3"){
      sendTextSet = "C3";
    }
    Send = true;
    
  }
  
}

void weight() {
  String data = String(get_units_kg()+offset, DEC_POINT);
  Serial.println(data);
  Serial.flush();
  delay(1000);
  
}

float get_units_kg() {
  return(scale.get_units()*0.453592);
  
}

void clockwise(){
  beltStepper.step(stepsPerRevolution);

}

void checkIR1() {
  ValIR1 = digitalRead(IR1);
  if (ValIR1 == 1) {
    wait1 = false;
  }
  if (ValIR1 == 0) {
    if (wait1 == false) {
      delay(1000);
      weight();
      wait1 = true;
    }
  }

}

void requestEvent() {
  if (Send == true) {
    Wire.print(sendTextSet);
    Send = false;
  }
}
