#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

int n; 
vector<pair<int, int>> selected; 
vector<pair<int, int>> lines; 


// void print_ans(){
//     for(auto a : ans)
//         cout << a << " ";
//     cout << endl; 
// }



bool overlapped(pair<int, int> l1, pair<int,int> l2){
    int a1, a2;
    tie(a1, a2) = l1;

    int b1, b2;
    tie(b1, b2) = l2;

    return  (a1 <= b1 && b1 <= a2) || (a1 <= b2 && b2 <= a2) ||
            (b1 <= a1 && a1 <= b2) || (b1 <= a2 && a2 <= b2) ;
}

bool possible(){
    for(int i = 0; i<(int)selected.size(); i++){
        for(int j = i+1; j<(int)selected.size(); j++){
            if (overlapped(selected[i], selected[j]))
                return false;
        }
    }
    return true;
}


void print_selected(){
    for(auto s : selected)
        cout << s.first << " " << s.second << " " << "|" <<" ";
    cout << endl;
}

int result = 0; 

void choose(int cnt){
    if (cnt == n){  
        if (possible()){
            // print_selected();
            result = max(result, (int)selected.size());
        }

        
        return;
    }

    selected.push_back(lines[cnt]);
    choose(cnt+1);
    selected.pop_back();

    choose(cnt+1);

}

int main() {

    cin >> n; 
    for (int i = 0; i < n; i++){
        int x1, x2;
        cin >> x1 >> x2; 
        lines.push_back(make_pair(x1, x2)); 
    }

    choose(0);
    cout << result;
    return 0;
}