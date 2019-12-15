char incomingByte; // for incoming serial data
int pin = 4;

void setup() {
  pinMode(pin, OUTPUT);
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    if(incomingByte == '1'){
      digitalWrite(pin, HIGH);
    }
    if(incomingByte == '0'){
      digitalWrite(pin, LOW);
    }

  }
}
