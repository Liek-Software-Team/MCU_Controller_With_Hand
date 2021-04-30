#include <Servo.h>
Servo motor;

void setup() {
  pinMode(8, OUTPUT);
  Serial.begin(9600);
  motor.attach(3);
}


void loop() 
{
  if(Serial.available())
  {
    char c = Serial.read();
    if(c == '1')
    {
    digitalWrite(8,HIGH);
    motor.write(180);
    delay(2000);
    }
    else if(c == '0')
    {
    digitalWrite(8,LOW);
    motor.write(0);
    delay(2000);
    }
  }
}
