#include <iostream>
using namespace std;

#define MAX_N 20
#define MAX_M 100 
#define D_DIR 8

int n, m;
int grid[MAX_N][MAX_N];


bool in_range(int x, int y){
    return x>=0 && x<n && y>=0 && y<n; 
}

pair<int, int> find_max(int x, int y){
    int dx[D_DIR] = {0, 1, 1, 1, 0, -1, -1, -1};
    int dy[D_DIR] = {1, 1, 0, -1, -1, -1, 0, 1};

    pair<int, int> pos = make_pair(x, y);
    int num = 0;

    
    

    for(int i = 0; i < D_DIR; i++){
        int nx = x+dx[i];
        int ny = y+dy[i];

        if (in_range(nx, ny) && grid[nx][ny] > num){
            num = grid[nx][ny];
            pos = make_pair(nx, ny);
        }
    }

    return pos;

}

void print_grid(){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void change(int x, int y){
    pair<int, int> np = find_max(x, y);
    
    int nx = np.first, ny = np.second;
    // cout << nx << " " << ny << endl << endl;
    int temp = grid[nx][ny];
    grid[nx][ny] = grid[x][y];
    grid[x][y] = temp;

    // print_grid();


}



int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m;

    for(int i = 0; i<n; i++)
        for(int j = 0; j<n; j++)
            cin >> grid[i][j];
    
    // print_grid();

    for(int num = 1; num<=(n*n); num++){
        bool key = true;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == num && key == true){
                    change(i, j);
                    key = false;    
                }
            }
        }

    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }

    
    return 0;
}