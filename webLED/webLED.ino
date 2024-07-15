int redPin = 5;
int bluePin = 6;
int LEDVal = 255;
String cmd;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
    
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() == 0){
    
  }
  cmd = Serial.readStringUntil('\r');
  if (cmd == "onRed"){
    analogWrite(redPin, LEDVal);
  }
  if (cmd == "onBlue"){
    analogWrite(bluePin, LEDVal);
  }
  if (cmd == "offRed"){
    analogWrite(redPin, 0);
  }
  if (cmd == "offBlue"){
    analogWrite(bluePin, 0);
  }
}