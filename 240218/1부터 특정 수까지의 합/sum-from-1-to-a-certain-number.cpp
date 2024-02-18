#include <iostream>

using namespace std;
 
int func(int a){
    int result = 0;
    for(int i=0; i<=a; i++){
        result += i;
    }

    return result/10;

}

int main() {
    // 여기에 코드를 작성해주세요.
    int input, result = 0;
    cin >> input;

    cout << func(input) ; 


    return 0;
}