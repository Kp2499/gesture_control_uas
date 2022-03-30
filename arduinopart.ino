 // button naming as per gamepad controller xbox 360
int flexSensor0=A0;
int flexSensor1=A1;
int flexSensor2=A2;

int sensorData0=0;
int sensorData1=0;
int sensorData2=0;

int sensorDataExact1=0;

void setup() {
Serial.begin(9600);
pinMode(flexSensor0,INPUT);
pinMode(flexSensor1,INPUT);
pinMode(flexSensor2,INPUT);
}

void loop() {

sensorData0=analogRead(flexSensor0);
sensorData1=analogRead(flexSensor1);
sensorData2=analogRead(flexSensor2);

//Serial.println(sensorData0);

if(sensorData0>840){
  sensorDataExact1=map(sensorData1, 840, 980, 12988, 32767);
  }

   
    if(sensorDataExact1>13200){
    Serial.print("Z");
    Serial.print(sensorDataExact1); // Left
    Serial.println();
    }
    else
    {
      Serial.println("R");// neutralling the Yaw jostick
    }

}
