#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

#define MAX_N 8
#define DIR_N 4

using namespace std;

int grid[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];

vector<pair<int, int>> city; // 모든 도시 좌표 저장
vector<pair<int, int>> selected; // 선택된 도시 좌표 저장
int n, k, u, d;

int dx[DIR_N] = {0, 1, 0, -1};
int dy[DIR_N] = {1, 0, -1, 0};

bool in_range(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < n;
}

void reset_visited() {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            visited[i][j] = false;
}

bool can_go(int x, int y, int nx, int ny) {
    if (!in_range(nx, ny) || visited[nx][ny])
        return false;
    
    int diff = abs(grid[x][y] - grid[nx][ny]);
    
    // 이동 가능 조건: 높이 차가 u 이상 d 이하
    if (diff >= u && diff <= d)
        return true;

    return false;
}

int bfs() {
    reset_visited();
    queue<pair<int, int>> q;

    // 선택된 도시들을 큐에 넣고 방문 처리
    for (auto s : selected) {
        q.push(s);
        visited[s.first][s.second] = true;
    }

    int count = 0;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        count++;

        for (int i = 0; i < DIR_N; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (can_go(x, y, nx, ny)) {
                q.push({nx, ny});
                visited[nx][ny] = true;
            }
        }
    }

    return count;
}

int result = 0;

void choose(int idx, int cnt) {
    // k개의 도시를 선택했을 경우
    if (cnt == k) {
        result = max(result, bfs()); // BFS를 실행하고 결과 갱신
        return;
    }

    if (idx >= n * n)
        return;

    // 도시 선택
    selected.push_back(city[idx]);
    choose(idx + 1, cnt + 1); // 다음 도시 선택
    selected.pop_back();

    // 도시 선택 안 함
    choose(idx + 1, cnt);
}

int main() {
    cin >> n >> k >> u >> d;

    // 도시 정보 입력 및 모든 도시 좌표 저장
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            city.push_back({i, j});
        }
    }

    // 도시 선택 및 탐색 시작
    choose(0, 0);

    // 결과 출력
    cout << result << endl;

    return 0;
}