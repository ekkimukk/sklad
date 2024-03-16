#include <sys/time.h>
#include <thread>
#include <chrono>
#include <time.h>
#include <string>
#include <map>
#include <iostream>
#include <ctime>
#include <cmath>
#include <cstdlib>
using namespace std;
std::chrono::duration<double> elapsed_seconds;

// Function to print an array
void printString(int arr[], int len)
{
  int i;
  for (i = 0; i < len; i++)
      cout << " " << arr[i];
}

// Function to generate the array
string makeString(int size)
{
  string str = "";
  string chars = "wigkh";
  for (int i; i < size; ++i) {
    str += chars[rand() % 5];
  }
  return str;
}

// Function to generate the substring
string makeSubstring(int substringSize)
{
  string substring = "";
  string chars = "wigkh";
  for (int i; i < substringSize; ++i) {
    substring += chars[rand() % 5];
  }
  return substring;
}

/* 1. Boyer-Meow string-search algorithm */
void BoyerMoore(string substring, int substringSize)
{
  map<char, int> meowTable = {};
  for (int i = 0; i < substringSize - 1; ++i) {
    meowTable[substring[i]] = i;
  }

  //cout << substring[i] << meowTable[substring[i]] << endl;

  for(map<string, pair<string,string> >::const_iterator it = meowTable.begin();
    it != meowTable.end(); ++it)
{
    std::cout << it->first << " " << it->second.first << " " << it->second.second << "\n";
}
}

void searches(string str, int size, int searchType)
{
  switch(searchType)
  {
    case 1: {
      break;
    } case 2: {
      break;
    } case 3: {
      break;
    } default: {
      break;
    }
  }
}

int main() 
{
  srand(time(0)); /* for array generation */

  int substringSize = 5;
  string substring = makeSubstring(substringSize);
  cout << substring  << endl;
    for (int size = 20; size <= 20; size += 100) {
      string str = makeString(size);
      for (int searchType = 1; searchType <= 1; ++searchType) {
        BoyerMoore(substring, substringSize);
      }
  }


  return 0;
}
