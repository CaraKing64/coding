#include <iostream>

using namespace std;


class A{
  public:
    A(){
      cout << "Created an A" << endl;
    };
    ~A(){
      cout << "Deleted an A" << endl;
    }
};
class B : public A{
  public:
    int id;
    B(): B(0){};
    B(int id){
      this->id = id;
      cout << "Created a B with id " << id << endl;
    };
    ~B(){
      cout << "Deleted a B with id " << id << endl;
    }
};
class C : public A{
  public:
    int id;
    C(): C(0){};
    C(int id){
      this->id = id;
      cout << "Created a C with id " << id << endl;
    };
    ~C(){
      cout << "Deleted a C with id " << id << endl;
    }
};

int main(){

  A* array = new A[2];
  cout << "MAKING A B" << endl;
  array[0] = B(5);

  cout << "MAKING A C" << endl;
  array[1] = C(69);

  cout << "testing IDs" << endl;
  cout << ((B) array[0]).id << endl;



  return 0;
}