void setup() {
 Serial.begin(9600);
 // the TX pin of Bolt is connected to the RX pin of Arduino Serial Port
 //and the TX pin of Bolt is connected to the TX pin of Arduino Serial Port  
}

void loop() {
  int temp_value, light_value;
  temp_value=analogRead(A0);//Reading temperature value at A0 pin of Arduino
  light_value=analogRead(A1);//Reading light sensor value at A1 pin of Arduino
  Serial.println(temp_value);
  Serial.println(light_value);
  delay(10000);
}
