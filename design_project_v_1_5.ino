// V 1.5 includes: 
// - Code for the button used to turn device on and off
// - Code for the RTC
// - Code for the LEDs
// - Mapping from amplitude to decibels and use of function to turn on LEDs

#include  <virtuabotixRTC.h>  // Library used for RTC
virtuabotixRTC myRTC(7, 8, 9); // myRTC(SCK, MISO, CS)

const int sampleWindow = 150;     // Sample window width in mS (150 mS)
int sample;

// Power
int powerButton = 4;
int powerLight = 6;

bool deviceOn = false;
int currentButton;
int lastButton;

// Notification LEDs
int greenLight = 11;
int yellowLight = 12; 
int redLight = 13;

// converting from amplitude (pk-pk) to decibels using the equation generated from calibration
int convertToDecibels(int peakVal) {                
    return (43.9 + 10.6*(log(peakVal) ));
}

boolean debounce(boolean last)
{
  boolean current = digitalRead(powerButton);
  if(last != current)
  {
    delay(5);
    current = digitalRead(powerButton);
  }
  return current;
}

void setup() {
    // Initialize serial communications
    Serial.begin(9600);
    
    // Function to set RTC's time, uncommment only if you want to reset it and change the time accordingly. 
//    myRTC.setDS1302Time(15, 31, 22, 2, 12, 7, 2022); // seconds, minutes, hours, day of the week, day of the month, month, year

    // Initialize power 
    pinMode(powerButton, INPUT);
    pinMode(powerLight, OUTPUT);
    
    // Initialize notification LEDs
    pinMode(greenLight, OUTPUT);
    pinMode(yellowLight, OUTPUT);
    pinMode(redLight, OUTPUT);
}

void loop() {
    // Check if power button has been pressed
    currentButton = debounce(lastButton);
    // comment out if to test without button functionality

    if(lastButton == LOW && currentButton == HIGH)
    {
      deviceOn = !deviceOn;
    }

    lastButton = currentButton;

    if(deviceOn == false)  // Device is off, LED light is off
    {
      digitalWrite(powerLight, LOW);
      digitalWrite(greenLight, LOW);
      digitalWrite(yellowLight, LOW);
      digitalWrite(redLight, LOW);
    }
    else                  // Device is on and running
    {
      digitalWrite(powerLight, HIGH);
      unsigned long startMillis= millis();                   // Start of sample window
      float peakToPeak = 0;                                  // peak-to-peak level
 
      unsigned int signalMax = 0;                            //minimum value
      unsigned int signalMin = 1024;                         //maximum value
      bool noBlinking = true;

      myRTC.updateTime();

      // Start printing elements as individuals
      Serial.print(myRTC.dayofmonth);
      Serial.print("/");
      Serial.print(myRTC.month);
      Serial.print("/");
      Serial.print(myRTC.year);
      Serial.print(" ");
      Serial.print(myRTC.hours);
      Serial.print(":");
      Serial.print(myRTC.minutes);
      Serial.print(":");
      Serial.println(myRTC.seconds);
                                                          // collect data for 150 mS
      while (millis() - startMillis < sampleWindow)
      {
          sample = analogRead(A0);                    //get reading from sound sensor
          if (sample < 1024)                                 
          {
             if (sample > signalMax)
             {
                signalMax = sample;                           // save max value
             }
             else if (sample < signalMin)
            {
                signalMin = sample;                           // save min value
            }
          } 
      }
   
      peakToPeak = signalMax - signalMin;                    // max - min = peak-peak amplitude
      Serial.println(peakToPeak);
      Serial.println(convertToDecibels(peakToPeak));
   
      // no LEDS on: less than 80 dB 
      if(convertToDecibels(peakToPeak) < 80) {
          digitalWrite(greenLight, LOW);
          digitalWrite(yellowLight, LOW);
          digitalWrite(redLight, LOW);
      }

      // green: 80 - 85 dB 
      if(convertToDecibels(peakToPeak) >= 80 && convertToDecibels(peakToPeak) < 85) {
          digitalWrite(greenLight, HIGH);
          digitalWrite(yellowLight, LOW);
          digitalWrite(redLight, LOW);
          
      } 
   
      // yellow: 85 - 95 dB  
      else if (convertToDecibels(peakToPeak) >= 85 && convertToDecibels(peakToPeak) < 95) {
          digitalWrite(yellowLight, HIGH);
          digitalWrite(greenLight, LOW);
          digitalWrite(redLight, LOW);
      }
   
     // red: 95 + 
     else if (convertToDecibels(peakToPeak) >= 95 && convertToDecibels(peakToPeak) < 110) {
          digitalWrite(redLight, HIGH);
          digitalWrite(yellowLight, LOW);
          digitalWrite(greenLight, LOW);
    }

     // fast red blinking: 110 + 
     else if (convertToDecibels(peakToPeak) >= 110) {
          noBlinking = false;
          digitalWrite(redLight, HIGH);
          delay(425);
          digitalWrite(redLight, LOW);
          delay(425);
          digitalWrite(yellowLight, LOW);
          digitalWrite(greenLight, LOW);
    }
    
    if(noBlinking) {
          delay(850);
    }
  } 
}
