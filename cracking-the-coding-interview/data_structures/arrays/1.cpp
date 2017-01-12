#include<iostream>
#include<cstring>
using namespace std;


string sortString(string s){
  char a;
  for (int i=0;i<s.length();i++) {
    for (int j=0;j<s.length();j++) {
      if (s[i]>s[j]) {
        a = s[i];
        s[i] = s[j];
        s[j] = a;
      }
    }
  }
  return s;
}

bool uniqueChar(string s){
  s = sortString(s);
  for (int i=0;i<s.length()-1;i++){
    if (s[i]==s[i+1]) {
      return false;
    }
  }
  return true;
}

bool uniqueChar2(string s){
  bool ascii[256];
  for (int i=0;i<s.length();i++){
    if (ascii[(int)s[i]]) {
      return false;
    }
    else {
      ascii[(int)s[i]]=true;
    }
  }
  return true;
}
int main() {
  string s = "qwferty*";
  cout<<uniqueChar(s)<<endl;
  cout<<uniqueChar2(s)<<endl;
  return 0;
}
