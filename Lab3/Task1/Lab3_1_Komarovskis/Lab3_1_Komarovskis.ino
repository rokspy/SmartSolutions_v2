
char test_data[100] = {0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,2};


void morseRead(char *data, char data_len);

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  morseRead(&test_data[0], sizeof(test_data)/sizeof(test_data[0]));
  delay(1000);
}

void morseRead(char *data, char data_len){
  int x;
  for (int k=0; k<data_len; k++){
    x = *data;
    if(x==2) break;
    digitalWrite(13, x);
    delay(200);
    data++;
  }
}
