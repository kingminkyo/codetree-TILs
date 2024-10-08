#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
#include <cmath>

#define MAX_N 100
#define DIR_N 4

using namespace std;

int grid[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];

vector<pair<int, int>> city; 
vector<pair<int, int>> selected;

queue<pair<int, int>> q; 

int n, k, u, d;

bool in_range(int x, int y){
    return x>=0 && x<n && y>=0 && y<n;
}

void reset_visited(){
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            visited[i][j] = false; 
}

void vector_to_q(){
    for (auto s : selected){
        q.push(s);
        visited[s.first][s.second] = true;
    }
}

bool can_go(int x, int y, int h1, int h2){
    if (!in_range(x, y))
        return false;

    int diff = abs(h1 - h2);
    
    if (visited[x][y] == true)
        return false;
    
    if (diff >= u && diff <= d)
        return true;
    
    return false;
}


void print_selected(){
    for(auto s : selected){
        cout << s.first << " " << s.second ;
    cout << endl; 
    }
}

int count_visited(){
    int count = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (visited[i][j] == true)
                count += 1;
        }
    }
    return count; 

}

void bfs(){
    int dx[DIR_N] = {0, 1, 0, -1};
    int dy[DIR_N] = {1, 0, -1, 0};

    while(!q.empty()){
        int x, y;
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for(int i = 0; i<DIR_N; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];

            if(can_go(nx, ny, grid[x][y], grid[nx][ny])){
                q.push(make_pair(nx, ny));
                visited[nx][ny] = true;
            }
        }


    }
}
void print_visited(){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cout << visited[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl; 
}

int result = 0; 

void choose(int idx, int cnt){
    if (cnt == k){
        reset_visited();
        vector_to_q();
        bfs();
        // print_selected();
        // print_visited();
        
        result = max(result, count_visited());

        // cout << result << endl; 
        return;
    }

    if (idx >= n*n)
        return;

    selected.push_back(city[idx]);
    choose(idx+1, cnt+1);
    selected.pop_back();

    choose(idx+1, cnt);

}



int main() {
    // 여기에 코드를 작성해주세요.

    cin >> n >> k >> u >> d;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> grid[i][j];
            city.push_back(make_pair(i, j));
            visited[i][j] = false;
        }
    }

    choose(0, 0);

    cout << result; 
    return 0;
}