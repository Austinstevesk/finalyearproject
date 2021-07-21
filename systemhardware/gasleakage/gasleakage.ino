#include <LCD_I2C.h> 
#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial sim(2, 3); //Rx, Tx
LCD_I2C lcd(0x27); // Default address of most PCF8574 modules, change accordingly
Servo motor;
String number = "+254797277217";

int gasValue = A0;
int buzzer = 13;
int Relay = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sim.begin(9600); //Synchronize gsm baudrate
  lcd.begin();
  lcd.backlight();
  motor.attach(5);
  motor.write(0);
  digitalWrite(Relay, HIGH);
  delay(3000);

}

void loop() {
  // put your main code here, to run repeatedly:
  int analogval = analogRead(gasValue);
  int data = (analogval-50)/10;
  motor.write(0);
  lcd.setCursor(2,0);
  lcd.print("Initializing");
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Gas Level: ");
  lcd.setCursor(10,0);
  lcd.print(data);
  lcd.setCursor(12,0);
  lcd.print("%");
  Serial.print("Gas Level: ");
  Serial.print(data);
  Serial.print("%");
  Serial.println();

  //Checking whether the gas level is high to trigger alert
  if(data>25){
    //digitalWrite(buzzer, HIGH);
    tone(buzzer, 100);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Gas Level: ");
    lcd.setCursor(10,0);
    lcd.print(data);
    lcd.setCursor(12,0);
    lcd.print("%");
    lcd.setCursor(3,1);
    lcd.print("DANGER!!");
    Serial.print("Gas Level: ");
    Serial.print(data);
    Serial.print("%");
    Serial.println();
    Serial.print("Setting measures-> Opening windows && Switching off mains");
    Serial.println();
    motor.write(90); //Open window
    sendSms(); //Send text message
    delay(5000);
    digitalWrite(Relay, LOW); //Power off mains
  }

 //Checking whether the gas value is normal to restore power
  else{
    //digitalWrite(buzzer, LOW);
    noTone(buzzer);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Gas Level");
    lcd.setCursor(10,0);
    lcd.print(data);
    lcd.setCursor(12,0);
    lcd.print("%");
    lcd.setCursor(0,1);
    lcd.print("Normal Level");
    Serial.print("Gas Level: ");
    Serial.print(data);
    Serial.print("%");
    Serial.println();
    motor.write(0);
    digitalWrite(Relay, HIGH);
    delay(2000);
  }

}

    void sendSms()
    {
      Serial.println ("Sending Message..........\n");
      sim.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
      delay(1000);
      //Serial.println ("Set SMS Number");
      sim.println("AT+CMGS=\"" + number + "\"\r"); //Mobile phone number to send message
      delay(1000);    
      String SMS = "Gas leakage! Setting measures";
      sim.println(SMS);
      Serial.println(SMS);
      Serial.println("sms sent");
      delay(100);
      sim.println((char)26);// ASCII code of CTRL+Z
      delay(1000);
   
    }
