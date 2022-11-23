#include <I2Cdev.h>
#include <Stepper.h>
#include <Wire.h>

String input;
const int rotate = 200;

Stepper columnStep(rotate, 10, 11, 12, 13);
Stepper rowStep(rotate, 6, 7, 8, 9);
Stepper inStep(rotate, 2, 3, 4, 5);

String inData;
String myArr[] = {"A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"};
int sizeArr = 9;
String newArr[9];
int i;
int count;

void setup(){
  columnStep.setSpeed(200);
  rowStep.setSpeed(200);
  inStep.setSpeed(200);
  Serial.begin(9600);
}

void loop(){
  while (count < 9) {
    if (sizeArr != 0) {
      sizeArr = sizeof(myArr)/sizeof(myArr[0]);
      input = myArr[0];
      ASRS(input);
      newArr[sizeArr - 1];
      for (i = 1; i < sizeArr; i++) {
        newArr[i - 1] = myArr[i];
      }
      myArr[sizeArr - 1];
      for (i = 0; i < sizeArr - 1; i++) {
        myArr[i] = newArr[i];
      }
    }
    count++;
  }
  delay(1000);
}

void ASRS(String input) {
  if (input == "A1") {
      Serial.println("A1");
      Pick();
      Move(250, 150); 
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
      Move(1100, 150);
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
      Move(1930, 1900);
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
