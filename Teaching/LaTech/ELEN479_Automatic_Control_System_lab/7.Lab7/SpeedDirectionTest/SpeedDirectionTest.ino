// Pins
#define PWM 9   // PWM pin to control motor speed
#define IN1 4   // IN1 and IN2 are two pins to control motor direction
#define IN2 5

void setup() {
  Serial.begin(115200);   // Set Communication rate
  pinMode(PWM,OUTPUT);    // Set PWM, IN1, and IN2 as output pins
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
}

void loop() {
  int pwr = 50; // speed command: 0 - 255; 0 is minimal; 255 is maximal (You can try different values here)
  int dir = 1; // The motor spins in different directions with dir = 1 and dir = -1.
  setMotor(dir, pwr, PWM, IN1, IN2);  // control the motor to spin with speed command and direction command. 
}

void setMotor(int dir, int pwmVal, int pwm, int in1, int in2){
  analogWrite(pwm,pwmVal); // Motor speed
  if(dir == 1){ 
    // Turn one way
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
  }
  else if(dir == -1){
    // Turn the other way
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
  }
  else{
    // Or dont turn
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);    
  }
}