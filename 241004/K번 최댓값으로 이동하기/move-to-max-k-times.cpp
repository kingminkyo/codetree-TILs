#include <iostream>
#include <queue>
#include <vector>

#define MAX_N 100
#define DIR_N 4 

using namespace std;


int grid[MAX_N][MAX_N];
bool can_visit[MAX_N][MAX_N];

queue<pair<int, int>> q; 

int n, k;
int r, c; 
int comp; 

bool in_range(int x, int y){
    return x>=0 && x<n && y>=0 && y<n; 
}

bool can_go(int x, int y, int num){
    if (!in_range(x, y))
        return false;
    if (grid[x][y]>=num || can_visit[x][y])
        return false;
    return true; 
}

void print_visit(){
    for (int i = 0; i < n; i++){
        for (int j = 0; j<n ; j++){
            cout << can_visit[i][j] << " "  ;
        }
    cout << endl; 
    }
}

void bfs(){
    int dx[DIR_N] = {0, 1, 0, -1};
    int dy[DIR_N] = {1, 0, -1, 0};

    while(!q.empty()){
        int x = q.front().first, y = q.front().second;
        // cout << x <<" "<< y << endl; 
        q.pop();

        for(int i = 0; i<DIR_N; i++){
            int nx = x+dx[i], ny = y+dy[i];

            if (can_go(nx, ny, comp)){
                // cout << nx << " " << ny << " " << comp << endl; 
                q.push(make_pair(nx, ny));
                can_visit[nx][ny] = true;
            }
        }
    }
}

void reset_visit(){
    for (int i = 0; i < n; i++){
        for (int j = 0; j<n; j++ ){
            can_visit[i][j] = false;
        }
    }
}

int main() {
    // 여기에 코드를 작성해주세요.

    cin >> n >> k ;
    for(int i = 0; i<n ; i++){
        for(int j = 0; j<n; j++){
            cin >> grid[i][j];
            can_visit[i][j] = false;
        }
    }
    cin >> r >> c ;
    r -= 1;
    c -= 1;

    for (int i = 0; i < k; i++){

    q.push(make_pair(r, c)); 
    comp = grid[r][c]; 

    bfs();

    int num = 0; 
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (can_visit[i][j] && grid[i][j] > num){
                num = grid[i][j];
                r = i;
                c = j; 
            }
        }
    }
    
    comp = grid[r][c]; 
    // cout << r << " " << c << comp << endl; 

    // print_visit();
    reset_visit();
    }
    // 
    cout << r+1 << " " << c+1 ; 
    // }



    return 0;
}