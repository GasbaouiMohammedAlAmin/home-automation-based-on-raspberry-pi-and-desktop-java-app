
void setup() {
 Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
   // Mesure la tension sur la broche A0
  float valeur_brute = analogRead(A0);
  
  // Transforme la mesure (nombre entier) en température via un produit en croix
  float temperature_celcius = (5* valeur_brute *100)/1024;
  
  // Envoi la mesure au PC pour affichage et attends 250ms
  Serial.println(temperature_celcius);
  
  delay(300);                       // wait for a second
}
