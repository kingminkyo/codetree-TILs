#include <iostream>
using namespace std;

void print_lines(int a, int b){
    for(int i = 0; i<a; i++){
        for (int j = 0; j<b; j++){
            cout << "1";
        }
        cout << endl ; 
    }
}


int main() {
    // 여기에 코드를 작성해주세요.
    int a, b = 0;
    cin >> a;
    cin >> b;

    print_lines(a, b);
    return 0;

}