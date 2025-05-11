#include <iostream>
#include <vector>
#include <string>



// Basic variable declarations
int myInt = 10;
double myDouble = 20.5;
char myChar = 'A';
bool myBool = true;
std::string myString = "Hello, World!";

// Core language features
void basicFeatures() {
  // Conditional statements
  if (myInt > 5) {
    std::cout << "myInt is greater than 5" << std::endl;
  } else {
    std::cout << "myInt is not greater than 5" << std::endl;
  }

  // Loops
  for (int i = 0; i < 5; ++i) {
    std::cout << "i: " << i << std::endl;
  }

  int j = 0;
  while (j < 5) {
    std::cout << "j: " << j << std::endl;
    ++j;
  }

  // Arrays and vectors
  int myArray[3] = {1, 2, 3};
  std::vector<int> myVector = {4, 5, 6};

  for (int k = 0; k < 3; ++k) {
    std::cout << "myArray[" << k << "]: " << myArray[k] << std::endl;
  }

  for (int val : myVector) {
    std::cout << "myVector value: " << val << std::endl;
  }
}

// Object-oriented syntax
class MyClass {
public:
  // Constructor
  MyClass(int value) : myValue(value) {}

  // Method
  void displayValue() const {
    std::cout << "Value: " << myValue << std::endl;
  }

  // Getter
  int getValue() const {
    return myValue;
  }

  // Setter
  void setValue(int value) {
    myValue = value;
  }

private:
  int myValue;
};

int main() {
  // Using basic features
  basicFeatures();

  // Using object-oriented features
  MyClass obj(10);
  obj.displayValue();
  obj.setValue(20);
  obj.displayValue();

  return 0;
}