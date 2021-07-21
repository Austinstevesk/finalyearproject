#include <LCD_I2C.h> 
#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial sim(2, 3); //Rx, Tx
SoftwareSerial gsm(2, 3); //Rx, Tx
LCD_I2C lcd(0x27); // Default address of most PCF8574 modules, change accordingly
Servo motor;
volatile int data;
String number = "+254743070455";
String user = "austin";
String resd = "Pangani";
int count = 0;

int gasValue = A0;
int buzzer = 13;
int Relay = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sim.begin(9600); //Synchronize gsm baudrate
  modem_init();
  data_init();
  internet_init();
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
  data = (analogval-50)/10;
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
    leakageCase(); //Send data as a leakage case
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
    send_data();
    nonLeakageCase(); //Send data as a non leakage case
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

    //Send data as a leakage case
void leakageCase(){
          String url;
      url = "http://austinstevesk.co.ke/gasmon/gasmon.php?username=";
      url += user;
      url += "residence=";
      url += resd;
      url += "gasValue=";
      url += data;
      url += "leakagecase=";
      url += 1;

      //url = "http://austinstevesk.co.ke/gasmon/gasmon.php?username=austin&residence=Kilimani&gasValue=39&leakagecase=1";

          
if (sim.available()){
  Serial.println("->");
  Serial.println("Sending data now");
    //Serial.write(gprsSerial.read());
 
  sim.println("AT");
 
  sim.println("AT+CPIN?");
  delay(1000);
 
  sim.println("AT+CREG?");
  delay(1000);
 
  sim.println("AT+CGATT?");
  delay(1000);
 
  sim.println("AT+CIPSHUT");
  delay(1000);
 
  sim.println("AT+CIPSTATUS");
  delay(2000);
 
  sim.println("AT+CIPMUX=0");
  delay(2000);
 
  ShowSerialData();
 
  sim.println("AT+CSTT=\"safaricom\"");//start task and setting the APN,
  delay(1000);
 
  //ShowSerialData();
 
  sim.println("AT+CIICR");//bring up wireless connection
  delay(3000);
 
  sim.println("AT+CIFSR");//get local IP adress
  delay(2000);
 
 
  sim.println("AT+CIPSPRT=0");
  delay(3000);

  Serial.println(url);
  sim.println(url);//begin send data to remote server
  
  ShowSerialData();
 
  sim.println((char)26);//sending
  delay(5000);//waiting for reply, important! the time is base on the condition of internet 

 
  ShowSerialData();
 
  sim.println("AT+CIPSHUT");//close the connection
  delay(100);

  }
}

  //Send data as a non-leakage case
void nonLeakageCase(){
          String url;
      url = "http://austinstevesk.co.ke/gasmon/gasmon.php?username=";
      url += user;
      url += "residence=";
      url += resd;
      url += "gasValue=";
      url += data;
      url += "leakagecase=";
      url += 0;

      //url = "http://austinstevesk.co.ke/gasmon/gasmon.php?username=austin&residence=Kilimani&gasValue=39&leakagecase=0";

          
if (sim.available()){
  Serial.println("->");
  Serial.println("Sending data now");
    //Serial.write(gprsSerial.read());
 
  sim.println("AT");
 
  sim.println("AT+CPIN?");
  delay(1000);
 
  sim.println("AT+CREG?");
  delay(1000);
 
  sim.println("AT+CGATT?");
  delay(1000);
 
  sim.println("AT+CIPSHUT");
  delay(1000);
 
  sim.println("AT+CIPSTATUS");
  delay(2000);
 
  sim.println("AT+CIPMUX=0");
  delay(2000);
 
  ShowSerialData();
 
  sim.println("AT+CSTT=\"safaricom\"");//start task and setting the APN,
  delay(1000);
 
  //ShowSerialData();
 
  sim.println("AT+CIICR");//bring up wireless connection
  delay(3000);
 
  sim.println("AT+CIFSR");//get local IP adress
  delay(2000);
 
 
  sim.println("AT+CIPSPRT=0");
  delay(3000);

  Serial.println(url);
  sim.println(url);//begin send data to remote server
  
  ShowSerialData();
 
  sim.println((char)26);//sending
  delay(5000);//waiting for reply, important! the time is base on the condition of internet 

 
  ShowSerialData();
 
  sim.println("AT+CIPSHUT");//close the connection
  delay(100);
}

else{
  while(count<1){
  Serial.println("Not sending data currently");
  count++;
  }
}

  }
void ShowSerialData()
{
  while(sim.available()!=0)
  Serial.write(sim.read());
  Serial.println("GPRS Available");
  //delay(5000); 
  
}

void modem_init()
{
  Serial.println("Please wait.....");
  gsm.println("AT");
  delay(1000);
  gsm.println("AT+CMGF=1");
  delay(1000);
  gsm.println("AT+CNMI=2,2,0,0,0");
  delay(1000);
}
void data_init()
{
  Serial.println("Please wait.....");
  gsm.println("AT");
  delay(1000); delay(1000);
  gsm.println("AT+CPIN?");
  delay(1000); delay(1000);
  gsm.print("AT+SAPBR=3,1");
  gsm.write(',');
  gsm.write('"');
  gsm.print("contype");
  gsm.write('"');
  gsm.write(',');
  gsm.write('"');
  gsm.print("GPRS");
  gsm.write('"');
  gsm.write(0x0d);
  gsm.write(0x0a);
  delay(1000); ;
  gsm.print("AT+SAPBR=3,1");
  gsm.write(',');
  gsm.write('"');
  gsm.print("APN");
  gsm.write('"');
  gsm.write(',');
  gsm.write('"');
  //------------APN------------//
  gsm.print("safaricom"); //APN Here
  //--------------------------//
  gsm.write('"');
  gsm.write(0x0d);
  gsm.write(0x0a);
  delay(1000);
  gsm.print("AT+SAPBR=3,1");
  gsm.write(',');
  gsm.write('"');
  gsm.print("USER");
  gsm.write('"');
  gsm.write(',');
  gsm.write('"');
  gsm.print("  ");
  gsm.write('"');
  gsm.write(0x0d);
  gsm.write(0x0a);
  delay(1000);
  gsm.print("AT+SAPBR=3,1");
  gsm.write(',');
  gsm.write('"');
  gsm.print("PWD");
  gsm.write('"');
  gsm.write(',');
  gsm.write('"');
  gsm.print("  ");
  gsm.write('"');
  gsm.write(0x0d);
  gsm.write(0x0a);
  delay(2000);
  gsm.print("AT+SAPBR=1,1");
  gsm.write(0x0d);
  gsm.write(0x0a);
  delay(3000);
}
void internet_init()
{
  Serial.println("Please wait.....");
  delay(1000);
  gsm.println("AT+HTTPINIT");
  delay(1000); delay(1000);
  gsm.print("AT+HTTPPARA=");
  gsm.print('"');
  gsm.print("CID");
  gsm.print('"');
  gsm.print(',');
  gsm.println('1');
  delay(1000);
}

void send_data()
{     
      String url;
      url = "http://austinstevesk.co.ke/gasmon/gasmon.php?username=";
      url += user;
      url += "&residence=";
      url += resd;
      url += "&gasValue=";
      url += data;
      url += "&leakagecase=";
      url += 0;

      //url = "http://austinstevesk.co.ke/gasmon/gasmon.php?username=austin&residence=Kilimani&gasValue=39&leakagecase=0";

      Serial.println(url);
  
  gsm.print("AT+HTTPPARA=");
//  gsm.print('"');
//  gsm.print("URL");
//  gsm.print('"');
//  gsm.print(',');
//  gsm.print('"');
//  gsm.print("http:");
//  gsm.print('/');
//  gsm.print('/');
  //-----------------------Your API Key Here----------------------//
  //Replace xxxxxxxxxxx with your write API key.
  gsm.println(url); 
  //---------------------------------------------------------------//
  Serial.println("Data sent");

  gsm.write(0x0d);
  gsm.write(0x0a);
  delay(1000);
  gsm.println("AT+HTTPACTION=0");
  delay(1000);
}
 
  
