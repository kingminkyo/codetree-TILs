#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_map>
using namespace std;

#define DIR_N 4
#define MAX_N 50

typedef tuple<int, int, int> Marble;

int t, n, m;
int marble_cnt[MAX_N][MAX_N];

int dx[DIR_N] = {-1, 0, 0, 1};
int dy[DIR_N] = {0, 1, -1, 0};

vector<Marble> marbles; 
unordered_map<char, int> d_dir; 

int grid[MAX_N][MAX_N]; 

bool in_range(int x, int y){
    return x>=0 && x<n && y>=0 && y<n;
}

void print_marbles(){
    int a, b, c; 
    for(auto m : marbles){
        tie(a, b, c) = m; 
        cout << a << " " << b << " " << c << " " << endl; 
    }
    cout << endl; 

}

Marble move(Marble marble){
    int x, y, dir;
    tie(x, y, dir) = marble;

    int nx = x+dx[dir];
    int ny = y+dy[dir];

    if (in_range(nx, ny))
        return make_tuple(nx, ny, dir);
    else    
        return make_tuple(x, y, 3-dir);
}

void move_all(){
    for(int i = 0; i < (int)marbles.size(); i++){
        marbles[i] = move(marbles[i]);
    }
}

void clear_all(){
    vector<Marble> temp;

    for(int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            grid[i][j] = 0;
        }
    }

    for(int i = 0; i < (int)marbles.size(); i++){
        int x, y;
        tie(x, y, ignore) = marbles[i];
        grid[x][y] += 1;
    }

    for(int i = 0; i < (int)marbles.size(); i++){
        int x, y;
        tie(x, y, ignore) = marbles[i];
        if (grid[x][y] == 1){
            temp.push_back(marbles[i]);
        }
    }

    marbles = temp;
}



void simulate(){
    
    move_all();
    clear_all(); 

}


int main() {
    // 여기에 코드를 작성해주세요.
    d_dir['U'] = 0;
    d_dir['R'] = 1;
    d_dir['L'] = 2;
    d_dir['D'] = 3;

    cin >> t;
    
    cin >> n >> m;

    for(int i = 1; i <= m; i++){
        int x, y; char d;
        cin >> x >> y >> d;
        marbles.push_back(make_tuple(x-1, y-1, d_dir[d]));

    }

    for(int i = 0; i < 2 * n; i++){
        simulate();
    }

    cout << (int)marbles.size(); 
    
    
    
    
    return 0;


}