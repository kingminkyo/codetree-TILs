#include <iostream>
#include <vector>
using namespace std;


vector<long long> arr; 
long long m; 

long long binary_search(long long target){
    long long left = 0;
    long long right = m-1;

    long long time = 0;

    while(left <= right){
        time += 1;
        long long mid = (left + right) / 2;

        if (arr[mid] == target)
            return time;
        if (arr[mid] > target)
            right = mid - 1;
        else
            left = mid + 1;

    }

}




int main() {
    // 여기에 코드를 작성해주세요.
    cin >> m; 

    for(long long i = 1; i <= m; i++){
        arr.push_back(i);
    }

    int a, b;
    cin >> a >> b;

    long long max_t = 0;
    long long min_t = 1000000; 
    for(long long i = a ; i <= b ; i++){
        long long time = binary_search(i);
        max_t = max(max_t, time);
        min_t = min(min_t, time);
    }

    cout << min_t << " " << max_t ;



    return 0;
}