#include <iostream>
#define INDEX 0 

using namespace std;

template <int SIZE, typename T>
class MyArray{
  public: 
    T array[SIZE];
};

int main(){
  MyArray<2, int> a;
  a.array[0] = 1;
  a.array[1] = 2;

  cout << a.array[INDEX] + a.array[INDEX + 1] << endl;
}