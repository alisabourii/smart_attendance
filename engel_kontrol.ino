int echo = 12;
int trig = 13;
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);


}

void loop() {
    int msf = Mesafe();
    //Serial.println(msf);
    if(msf < 15){
      Serial.println("A");
      digitalWrite(2,1);
    }
    else
      digitalWrite(2,0);
  delay(100);
}

int Mesafe(){
  digitalWrite(trig,1);
  delay(1);
  digitalWrite(trig,0);

  int sure = pulseIn(echo,1);
  int msf = (sure/2)/28.97;
  return msf;
}