#include <iostream>

using namespace std;

int gudub (int x, int y){

    int result = 1;
    for(int i = 0; i<y ; i++){
        result *= x;
    }
    return result;

}


int main() {
    // 여기에 코드를 작성해주세요.
    
    int a, b = 0;


    cin >> a;
    cin >> b;
    
    
    cout << gudub(a, b);

    return 0;
}