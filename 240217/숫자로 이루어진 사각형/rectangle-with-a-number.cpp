#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int input = 1;
    cin >> input;
    int number = 1; 
    for (int i=0; i<input ; i++){
        for ( int j=0; j<input ; j++){
            if (number == 10) number = 1;
            cout << number << " " ; 
            number +=1; 
        }
        cout << endl;
    }

    return 0;
}