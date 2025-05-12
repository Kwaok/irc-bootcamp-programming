#include <Servo.h>

Servo myservo;
int angle = 0;
int lamp_button = 12;
int lamp = 7;
int servo_button = 11;
int hand = 4;

void setup() {
  myservo.attach(4);
  pinMode(lamp_button, INPUT);
  pinMode(lamp, OUTPUT);
  pinMode(servo_button, INPUT);
  pinMode(hand, OUTPUT);
  /**/
}

// the loop function runs over and over again forever
void loop() {
  if(digitalRead(lamp_button) == HIGH) {
    digitalWrite(lamp, HIGH);  
    delay(1000);                      
    digitalWrite(lamp, LOW);   
    delay(1000);                      
  }
  else {
    digitalWrite(lamp, LOW);
  }

  if(digitalRead(servo_button) == HIGH) {
    for(angle = 0; angle <= 180; angle++) {
      myservo.write(angle);
      delay(10);
    }
    
    for(angle = 180; angle >= 0; angle--) {
      myservo.write(angle);
      delay(10);
    }       
  }
}