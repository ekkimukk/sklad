#include <sys/time.h>
#include <thread>
#include <chrono>
#include <time.h>
#include <string>
#include <iostream>
#include <ctime>
#include <cmath>
#include <cstdlib>
using namespace std;

std::chrono::duration<double> elapsed_seconds;

// Function to print an array
void printArray(int arr[], int len)
{
  int i;
  for (i = 0; i < len; i++)
      cout << " " << arr[i];
}

// Function to generate the array
void makeArray(int *arr, int len) {
  for (int i = 0; i < len; ++i) {
    arr[i] = 1 + rand() % 2000;
  }
}

/* 1 */
void bubbleSort(int *arr, int len)
{
  for (size_t i = 0; i + 1 < len; ++i) {
    for (size_t j = 0; j + 1 < len - i; ++j) {
      if (arr[j + 1] < arr[j]) {
        swap(arr[j], arr[j + 1]);
      }
    }
  }
}

/* 2 */
void qSort(int *mas, int size) {
    int i = 0;
    int j = size - 1;
    int mid = mas[size / 2];
    do {
        while (mas[i] < mid) {
            i++;
        }
        while (mas[j] > mid) {
            j--;
        }
        if (i <= j) {
            int tmp = mas[i];
            mas[i] = mas[j];
            mas[j] = tmp;
            i++;
            j--;
        }
    } while (i <= j);
    if (j > 0) {
        qSort(mas, j + 1);
    }
    if (i < size) {
        qSort(&mas[i], size - i);
    }
}

/* 3 */
void heapify(int arr[], int n, int i) {
  // Find largest among root, left child and right child
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;
  if (left < n && arr[left] > arr[largest])
    largest = left;
  if (right < n && arr[right] > arr[largest])
    largest = right;
  // Swap and continue heapifying if root is not largest
  if (largest != i) {
    swap(arr[i], arr[largest]);
    heapify(arr, n, largest);
  }
}
// main function to do heap sort
void heapSort(int arr[], int n) {
  // Build max heap
  for (int i = n / 2 - 1; i >= 0; i--)
    heapify(arr, n, i);
  // Heap sort
  for (int i = n - 1; i >= 0; i--) {
    swap(arr[0], arr[i]);
    // Heapify root element to get highest element at root again
    heapify(arr, i, 0);
  }
}


void sorts(int *arr, int len, int sortType) 
{
  //for (int sortType = 1; sortType <= 3; ++sortType) {
    switch(sortType)
    {
      case 1: {
        auto start = std::chrono::system_clock::now();
        bubbleSort(arr, len);
        auto end = std::chrono::system_clock::now();
        elapsed_seconds += end-start;
        //cout << "\nBubble Sort >> "<< "elapsed time: " << elapsed_seconds.count() << "s" << endl;
        break;
      }
      case 2: {
        auto start = std::chrono::system_clock::now();
        qSort(arr, len);
        auto end = std::chrono::system_clock::now();
        elapsed_seconds += end-start;
        //cout << "\nQuick Sort >> "<< "elapsed time: " << elapsed_seconds.count() << "s" << endl;
        break;
      }
      case 3: {
        auto start = std::chrono::system_clock::now();
        heapSort(arr, len);
        auto end = std::chrono::system_clock::now();
        elapsed_seconds += end-start;
        //cout << "\nHeap Sort >> "<< "elapsed time: " << elapsed_seconds.count() << "s" << endl;
        break;
      }
    }
  //}
}

int main() 
{
  srand(time(0)); /* for array generation */
  int len = 0;
  for (len; len <= 2000; len += 50) {
    int arr[len];

    for (int sortType = 2; sortType <= 2; ++sortType) {
      elapsed_seconds = std::chrono::system_clock::now() - std::chrono::system_clock::now();
      int repeats = 10000;
      for (int i = 0; i < repeats; ++i) {
        makeArray(arr, len);
        sorts(arr, len, sortType);
        //printArray(arr, len);
      }
      //auto sumT = std::chrono::system_clock::now() - std::chrono::system_clock::now();
      //cout << ">>>>>" << sumT.count() << endl;
      if (sortType == 1) {
        //cout << "Bubble Sort" << endl << "Repeats=" << repeats << " " << "Time=";
        elapsed_seconds /= 10000;
        //cout << len << " >> " << elapsed_seconds.count() << endl;
        cout << elapsed_seconds.count() << endl;
      } else if (sortType == 2) {
        //cout << "Quick Sort" << endl << "Repeats=" << repeats << " " << "Time=";
        elapsed_seconds /= 10000;
        //cout << elapsed_seconds.count() << endl;
        //cout << len << " >> " << elapsed_seconds.count() << endl;
        cout << elapsed_seconds.count() << endl;
      } else if (sortType == 3) {
        //cout << "Heap Sort" << endl << "Repeats=" << repeats << " " << "Time=";
        elapsed_seconds /= 10000;
        //cout << elapsed_seconds.count() << endl;
        //cout << len << " >> " << elapsed_seconds.count() << endl;
        cout << elapsed_seconds.count() << endl;
      } else { return 1; }
    }

  }

  return 0;
}
