#include <iostream>
#include <vector>
using namespace std;

int n = 0 ; 
vector<int> arr;

void printArr(){
    for (int i=0; i<arr.size(); i++)
        cout << arr[i] << " ";
    cout << endl;
}

bool isBeautiful(){
    for (int i=0; i<arr.size(); i+=arr[i]){

        // if(i + arr[i] - 1 >= n)
        //     return false;
        // printArr();
        for (int j = i; j < i+arr[i]; j++){
            if (arr[j] != arr[i]){
                return false;
            }
        }



    }

    // printArr();
    return true;
}





int result = 0; 

void choose(int cnt){

    if (cnt == n){
        // printArr();
        if (isBeautiful())
            result++; 
        return ;
    }

    for(int i=1; i<5; i++){
        arr.push_back(i);
        choose(cnt+1);
        arr.pop_back();
    }
}





int main() {
    // 여기에 코드를 작성해주세요.

    cin >> n ; 
    choose(0);

    cout << result; 
    return 0;
}