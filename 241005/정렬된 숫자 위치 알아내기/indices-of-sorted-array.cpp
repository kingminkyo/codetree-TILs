#include <iostream>
#include <algorithm>
#include <vector> 

using namespace std;

class Number{
    public:
        int number; 
        int index; 
        Number(int num, int idx){
            this->number = num;
            this->index = idx;
        }
        Number(){}
};

vector<Number> numbers;
int n; 
int num;

bool comp(Number a, Number b){
    if(a.number != b.number)
        return a.number < b.number;
    return a.index < b.index; 
}

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> num;         
        numbers.push_back(Number(num, i));
    }

    sort(numbers.begin(), numbers.end(), comp);

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(numbers[j].index == i)
                cout << j+1 << " ";
        }
    }

    return 0;
}