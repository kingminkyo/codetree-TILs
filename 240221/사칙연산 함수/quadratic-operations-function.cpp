#include <iostream>
#include <string.h>

using namespace std;
int cal(int a, int b, string c){

    if (!((c  == "+" ) || (c  == "-" ) || (c  == "/" ) || (c  == "*" ))){
        return false;
    } 
    else if (c == "+")
        return a+b;
    else if (c == "-")
        return a-b;
    else if (c == "/")
        return a/b;
    else if (c == "*")
        return a*b;
}
int main() {
    // 여기에 코드를 작성해주세요.

    int a, b = 0;
    string c ;

    cin >> a;
    cin >> c;
    cin >> b;

    if (cal(a, b, c)){
        cout << a << " " << c << " " << b << " = " << cal(a, b, c) ;
    }
    else{
        cout << "False";
    }
    
    return 0;
}