#include <I2Cdev.h>
#include <Stepper.h>
#include <Wire.h>

String input;
const int rotate = 200;

Stepper columnStep(rotate, 10, 11, 12, 13);
Stepper rowStep(rotate, 6, 7, 8, 9);
Stepper inStep(rotate, 2, 3, 4, 5);

void setup() {
  columnStep.setSpeed(200);
  rowStep.setSpeed(200);
  inStep.setSpeed(200);
  Wire.begin(8); 
  Serial.begin(9600);  
}
 
void loop() {
  Wire.requestFrom(8, 2);   

  if (Wire.available()) { 
    input = Wire.readString();
    Serial.println(input);
    if (input == "A1") {
      Serial.println("A1");
      Pick();
      Move(250, 170); 
    } else if (input == "A2") {
      Serial.println("A2");
      Pick();
      Move(250, 1000);
    } else if (input == "A3") {
      Serial.println("A3");
      Pick();
      Move(250, 1900);
    } else if (input == "B1") {
      Serial.println("B1");
      Pick();
      Move(1100, 170);
    } else if (input == "B2") {
      Serial.println("B2");
      Pick();
      Move(1100, 1000);
    } else if (input == "B3") {
      Serial.println("B3");
      Pick();
      Move(1100, 1900);
    } else if (input == "C1") {
      Serial.println("C1");
      Pick();
      Move(1930, 150);
    } else if (input == "C2") {
      Serial.println("C2");
      Pick();
      Move(1930, 1000);
    } else if (input == "C3") {
      Serial.println("C3");
      Pick();
      Move(1930, 1915);
    }
  }
}

void Pick() {
  Serial.println("Picking...");
  inStep.step(725);
  delay(1000);
}

void Move(int column, int row) {
  Serial.println("Moving...");
  rowStep.step(row);
  delay(1000);
  columnStep.step(column);
  delay(1000);
  Place();
  Serial.println("Returning...");
  rowStep.step(-row);
  delay(1000);
  columnStep.step(-column);
  delay(1000);
}

void Place() {
  Serial.println("Storing...");
  inStep.step(800);
  delay(1000);
  rowStep.step(-100);
  delay(1000);
  inStep.step(-800);
  delay(1000);
  rowStep.step(100);
  delay(1000);
  inStep.step(-725);
  delay(1000);
}
