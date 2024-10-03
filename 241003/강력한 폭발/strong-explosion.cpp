#include <iostream>
#include <tuple>
#include <vector>

using namespace std;


#define MAX_N 20

int n;
int bomb_type[MAX_N][MAX_N];
bool bombed[MAX_N][MAX_N];

int ans;


bool inRange(int x, int y){
    return x>=0 && x<n && y>=0 && y<n; 
}
void Bomb(int x, int y, int b_type){
    pair<int, int> bomb_shape[3][5] = {
        {{-2, 0},{-1, 0},{0, 0}, {1, 0}, {2, 0}},
        {{1, 0}, {-1, 0}, {0, 0}, {0, 1}, {0, -1}},
        {{1, 1}, {-1, 1}, {0, 0}, {1, -1}, {-1, -1}}
    };

    for (int i = 0; i < 5; i++){
        int dx, dy;
        tie(dx, dy) = bomb_shape[b_type][i];

        int nx = x+dx, ny = y+dy;
        if(inRange(nx, ny))
            bombed[nx][ny] = true;
    }
}

int Calc(){
    for(int i = 0; i<n; i++)
        for(int j=0; j<n; j++)
            bombed[i][j] = false;

    
    for(int i = 0; i<n; i++)
        for(int j=0; j<n; j++)
            if(bomb_type[i][j])
                Bomb(i, j, bomb_type[i][j]);
    
    int cnt = 0;
    for(int i = 0; i<n; i++)
        for(int j=0; j<n; j++)
            if(bombed[i][j])
                cnt++;
    return cnt;


}
vector<pair<int, int>> bomb_pos;
void choose(int cnt){
    if (cnt == (int) bomb_pos.size()){
        ans = max(ans, Calc());
        return;
    }

    for(int i = 0; i<3; i++){
        int x, y;
        tie(x, y) = bomb_pos[cnt];

        bomb_type[x][y] = i;
        choose(cnt+1);
        bomb_type[x][y] = 0;
    }
}




int main() {
    // 여기에 코드를 작성해주세요.

    cin >> n;

    for (int i = 0; i<n ; i++){
        for (int j = 0; j<n ; j++){
            int place;
            cin >> place;
            if(place){
                bomb_pos.push_back(make_pair(i, j));
            }
        }


    }
    choose(0);
    cout << ans; 
    return 0;
}