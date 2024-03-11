#include <iostream>
#include <cmath>
using namespace std;

double 
min(double *arr)
{
  double res = 1000;
  for (int i = 0; i < 95; ++i){
    if (arr[i] < res) { res = arr[i]; }
  }
  return res;
}

double 
max(double *arr)
{
  double res = 0;
  for (int i = 0; i < 95; ++i){
    if (arr[i] > res) { res = arr[i]; }
  }
  return res;
}

double 
mid(double *arr)
{
  double res = 0;
  for (int i = 0; i < 95; ++i) {
    res += arr[i];
  }
  return res/95;
}

int 
main() 
{
  double 
  array[95] = {40.1, 44.3,	46.2,	34.8,	31.1,	15,	  42.3,	25.7,	42,
               31.9, 45.5,	38.7,	38.7,	47.2,	46.2,	47.5,	48,	  35.5,
               37.6, 57.1,	40.1,	58.6,	27.6,	51.3,	36.9,	49.6,	31.3,
               43,	 2.9,	  31.8,	39.3,	37.4,	45,  	34.4,	54.9,	38.8,
               49.1, 50.9,	43.7,	57, 	36.5,	28.9,	34.4,	35, 	51.9,
               46.2, 44.4,	40.4,	32, 	33.6,	45.4,	56.8,	41.7,	43.2,
               42.1, 52.4,	36.1,	57.6,	33.4,	64.3,	44, 	50.7,	27.3,
               31.5, 45.2,	34.2,	33.2,	35.6,	33, 	38.7,	26.1,	
               45.6, 29.6,	36, 	31.1,	58.8,	20.1,	58, 	38.4,
               52.7, 45.3,	38,	  36,	  46.6,	44.9,	64.4,	38.2,
               16,   39.4,	34,	  49.1,	40.6,	46.1,	27.8,	46.4};

  /* 1 */
  printf("Oбъем выборки = %d\n", 95);

  /* 2 */
  printf("Xmin = %f\nXmax = %f\nR = %f\n", min(array), max(array), max(array)-min(array));

  /* 3 */
  printf("Медиана = %f\nМода = %f\n", mid(array), 46.2);
  
  /* 4 */
  printf("Число интервалов разбиения = %f\n", 1 + 3.322 * log10(95));
  printf("Длина интервала разбиения = %f\n", (max(array)-min(array))/(1 + 3.322 * log10(95)));


  return 0;
}

