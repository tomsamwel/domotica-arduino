//start LDR part
const int ldrPin = A0;


//timers om te kijken of een bepaald tijdpunt voorbij is
long previousMillis = 0;
long previousMillis2 = 0;
long interval = 5000;
long interval2 = 5500;

//aanroepen van de pins van de led
const int redPin = 2;
const int greenPin = 3;

//houdt later de waarde van de LDR vast
int analogValue = 0;

//zet rood aan, groen uit
void redLight(){
  digitalWrite(redPin, HIGH);
  digitalWrite(greenPin, LOW);
}
//zet groen aan, rood uit
void greenLight(){
  digitalWrite(redPin, LOW);
  digitalWrite(greenPin, HIGH);
}



//eind LDR part

void setup() {
  //start serial monitor
  Serial.begin(9600);
  //lampjes staan in het begin uit
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
}

void loop() {
  //zet de waarde van de LDR in de 
  int analogValue = analogRead(A0);

  //zet een timestamp voor het versturen van de waarde
  unsigned long Millis = millis();
  //wanneer de wachttijd voorbij is, wordt de waarde verstuurd
  if(Millis - previousMillis > interval){
    previousMillis = Millis;
    Serial.println(analogValue);
  }
  
  
  //zet een timestamp voor het ophalen van de waarde
  unsigned long Millis2 = millis();
  //wanneer de wachttijd voorbij is, wordt de waarde opgehaald, omgezet naar een integer en wordt er gekeken naar of de verlichting aan of uit moet
  if(Millis2 - previousMillis2 > interval2){
    previousMillis2 = Millis2;
    byte data = Serial.read();
    int a_data = data;
    if(analogValue > a_data){
      delay(50);
    redLight();
    } 
    else
    {
      delay(50);
      greenLight();
    }
  }
}
