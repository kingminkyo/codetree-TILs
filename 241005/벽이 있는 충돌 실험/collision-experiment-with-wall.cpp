#include <iostream>
#include <tuple>
#include <vector>
#include <unordered_map>

#define DIR_NUM 4
#define MAX_N 50

using namespace std;

typedef tuple<int, int, int> Marble;

// 전역 변수 선언:
int t, n, m;

int grid[MAX_N + 1][MAX_N + 1]; // marble_cnt 대신 grid 사용

unordered_map<char, int> d_dir; // mapper 대신 unordered_map 사용

// dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록 설정합니다.
int dx[DIR_NUM] = {-1, 0, 0, 1};
int dy[DIR_NUM] = {0, 1, -1, 0};

vector<Marble> marbles;

// 해당 위치가 격자 안에 들어와 있는지 확인합니다.
bool InRange(int x, int y) {
    return 1 <= x && x <= n && 1 <= y && y <= n;
}

// 해당 구슬이 1초 후에 어떤 위치에서 어떤 방향을 보고 있는지를 구해
// 그 상태를 반환합니다.
Marble Move(Marble marble) {
    int x, y, dir;
    tie(x, y, dir) = marble;

    // 바로 앞에 벽이 있는지 판단합니다.
    int nx = x + dx[dir], ny = y + dy[dir];
    
    // Case 1 : 벽이 없는 경우에는 그대로 한 칸 전진합니다.
    if(InRange(nx, ny))
        return make_tuple(nx, ny, dir);
    // Case 2 : 벽이 있는 경우에는 방향을 반대로 틀어줍니다.
    else
        return make_tuple(x, y, 3 - dir);
}

// 구슬을 전부 한 번씩 움직여 봅니다.
void MoveAll() {
    for(int i = 0; i < (int) marbles.size(); i++)
        marbles[i] = Move(marbles[i]);
}

// 해당 구슬과 충돌이 일어나는 구슬이 있는지 확인합니다.
// 이를 위해 자신의 현재 위치에 놓인 구슬의 개수가 
// 자신을 포함하여 2개 이상인지 확인합니다.
bool DuplicateMarbleExist(int target_idx) {
    int target_x, target_y;
    tie(target_x, target_y, ignore) = marbles[target_idx];

    return grid[target_x][target_y] >= 2; // grid로 구슬 개수 확인
}

// 충돌이 일어나는 구슬은 전부 지워줍니다.
void RemoveDuplicateMarbles() {
    vector<Marble> temp_vector;
    
    // Step2-1 : 각 구슬의 위치에 count를 증가시킵니다.
    for(int i = 0; i < (int) marbles.size(); i++) {
        int x, y;
        tie(x, y, ignore) = marbles[i];
        grid[x][y]++; // grid에 구슬 위치 카운트
    }

    // Step2-2 : 충돌이 일어나지 않는 구슬만 전부 기록합니다.
    for(int i = 0; i < (int) marbles.size(); i++)
        if(!DuplicateMarbleExist(i))
            temp_vector.push_back(marbles[i]);

    // Step2-3 : 나중을 위해 각 구슬의 위치에 적어놓은 count 수를 다시 초기화합니다.
    for(int i = 0; i < (int) marbles.size(); i++) {
        int x, y;
        tie(x, y, ignore) = marbles[i];
        grid[x][y]--; // grid 초기화
    }

    // step2-4 : 충돌이 일어나지 않은 구슬들로 다시 채워줍니다.
    marbles = temp_vector;
}

// 조건에 맞춰 시뮬레이션을 진행합니다.
void Simulate() {
    // Step1
    // 구슬을 전부 한 번씩 움직여 봅니다.
    MoveAll();

    // Step2
    // 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
    RemoveDuplicateMarbles();
}

int main() {
    // 방향 설정을 위한 unordered_map 초기화
    d_dir['U'] = 0;  // 위
    d_dir['R'] = 1;  // 오른쪽
    d_dir['L'] = 2;  // 왼쪽
    d_dir['D'] = 3;  // 아래

    // 테스트 케이스 수 입력:
    cin >> t;

    while(t--) {
        // 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
        marbles.clear();

        // 입력:
        cin >> n >> m;
        for(int i = 1; i <= m; i++) {
            int x, y; char d;
            cin >> x >> y >> d;
            marbles.push_back(make_tuple(x, y, d_dir[d]));
        }

        // 2*n번 이후에는 충돌이 절대 일어날 수 없으므로
        // 시뮬레이션을 총 2*n번 진행합니다.
        for(int i = 1; i <= 2 * n; i++)
            Simulate();
        
        // 출력:
        cout << (int) marbles.size() << endl;
    }

    return 0;
}