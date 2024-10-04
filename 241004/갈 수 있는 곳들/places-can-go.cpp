#include <iostream>
#include <vector>
#include <queue>

#define MAX_N 100
#define DIR_N 4

int grid[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];

int n, k;

queue<pair<int, int>> q;

using namespace std;

bool in_range(int x, int y){
    return x>=0 && x<n && y>=0 && y<n; 
}

bool can_go(int x, int y){
    if (!in_range(x, y))
        return false;
    if (grid[x][y] || visited[x][y])
        return false;
    return true; 
}

void bfs(){
    int dx[DIR_N] = {0, 1, 0, -1};
    int dy[DIR_N] = {1, 0, -1, 0};

    while(!q.empty()){
        pair<int, int> cp = q.front();
        int x = cp.first, y = cp.second;
        q.pop();

        for(int i = 0; i<DIR_N; i++){
            int nx = x+dx[i], ny = y+dy[i];

            if(can_go(nx, ny)){
                q.push(make_pair(nx, ny));
                visited[nx][ny] = true; 
            }

        }

    }



}

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> k ;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> grid[i][j];
        }
    }


    for(int i = 0; i < k; i++){
        int r, c;
        cin >> r >> c; 

        q.push(make_pair(r-1, c-1));
        visited[r-1][c-1] = true; 

    }
    bfs();

    int ans = 0;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if (visited[i][j])
                ans++; 
        }
    }

    cout << ans; 

    return 0;
}