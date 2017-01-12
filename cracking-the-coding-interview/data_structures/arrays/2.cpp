#include<iostream>
using namespace std;

int lenChar(char* s) {
  int count = 0;
  while (s[count]!='\0') {
    count++;
  }
  return count;
}

void reverse(char* str) {
  return;
}

int main() {
  char t[3] = {'d','d'};
  char* s = &t[0];
  if (t[2]=='\0') {
    int a = 3/2;
    printf("%d",lenChar(s));
    printf("%s",s[2]);
  }
}
