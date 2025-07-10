#include <iostream>
#include <chrono>

using namespace std;

int fibonacci(int n){
  switch (n){
    case 0:
    case 1:
      return 0;
    case 2:
      return 1;
    default:
      return fibonacci(n-1) + fibonacci(n-2);
  }
}

long long fibonacci_2(int n){
  if (n == 1){
    return 0;
  }
  long long temp;
  long long n1 = 0;
  long long n2 = 1;
  for (int i = 0; i < n-2; i++){
    temp = n1;
    n1 = n2;
    n2 = temp + n1;
  }
  return n2;
}

int main(){

  const int MAX_ITER = 20;

  auto start = chrono::high_resolution_clock::now();
  for (int i = 1; i < MAX_ITER; i ++){
    fibonacci(i);
  }
  auto stop = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(stop - start); 
  cout << "Fibonacci 1: "  << duration.count() << endl; 


  start = chrono::high_resolution_clock::now();
  for (int i = 1; i < MAX_ITER; i ++){
    fibonacci_2(i);
  }
  stop = chrono::high_resolution_clock::now();
  duration = chrono::duration_cast<chrono::microseconds>(stop - start); 
  cout << "Fibonacci 2: "  << duration.count() << endl; 
}