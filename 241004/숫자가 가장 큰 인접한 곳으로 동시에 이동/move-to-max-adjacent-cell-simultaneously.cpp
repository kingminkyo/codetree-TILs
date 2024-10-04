#include <iostream>
#include <vector>

#define DIR_NUM 4
#define MAX_N 20 

using namespace std;

int t, n, m; 

int grid[MAX_N][MAX_N];
int count[MAX_N][MAX_N];
int next_count[MAX_N][MAX_N];


bool in_range(int x, int y){
    return x>=0 && x<n && y>=0 && y<n; 
}

void print_count(){
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            cout << count[i][j] << " ";
        cout << endl; 
    cout << endl; 
}

pair<int, int> find_pos(int x, int y){
    int dx[DIR_NUM] = {-1, 1, 0, 0};
    int dy[DIR_NUM] = {0, 0, -1, 1};

    int num = 0; 
    pair<int, int> pos; 

    for (int i=0; i<DIR_NUM; i++){
        int nx = x+dx[i];
        int ny = y+dy[i];

        if(in_range(nx, ny) && grid[nx][ny] > num){
            num = grid[nx][ny];
            pos = make_pair(nx, ny);
        }
    }

    return pos;
}

void move(int x, int y){
    pair<int, int> np = find_pos(x, y);
    int nx = np.first, ny = np.second;

    next_count[nx][ny]++; 
}

void move_all(){
    for (int i = 0; i<n; i++)
        for (int j = 0; j < n; j++)
            next_count[i][j] = 0;
    
    for (int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            if (count[i][j] == 1)
                move(i, j);

    for (int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            count[i][j] = next_count[i][j];

    for (int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            if(count[i][j] >= 2)
                count[i][j] = 0;
}




void simulate(){
    move_all();
}

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m >> t;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> grid[i][j];

    for (int i = 0; i < m; i++){
        int x, y;
        cin >> x >> y;
        count[x-1][y-1] = 1;
    }


    for (int i = 0; i<t; i++){
        move_all();
    }

    int result = 0;

    for (int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            if (count[i][j] == 1)
                result += 1;
    
    cout << result;

    return 0;
}