#include <iostream>
using namespace std;

int n;
int grid[20][20];

int getGold(int row, int col){
    int count = 0;

    for(int i = row; i <= row+2 ; i++){
        for(int j = col; j <= col+2; j++){
            count += grid[i][j];
        }
    }
    return count ;

}

int main() {
    // 여기에 코드를 작성해주세요.


    int result = 0;

    cin >> n;
    for(int i = 0; i < n; i++ )
        for(int j = 0; j<n; j++)
            cin >> grid[i][j];

    
    int count = 0;

    for(int i = 0; i < n-2 ; i++){
        for(int j = 0; j < n-2 ; j++){

            
            result = getGold(i, j);
            // cout << i << " " << j << " " << result << endl; 
            count = max(result, count );

        }
    }

    cout << count;
    





    return 0;
}