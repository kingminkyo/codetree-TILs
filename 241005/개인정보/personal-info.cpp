#include <iostream>
#include <algorithm>

using namespace std;

#define MAX_N 5

class Student{
    public:
        string name;
        int height;
        double weight;

        Student(string name, int height, double weight){
            this->name = name;
            this->height = height;
            this->weight = weight;
        }
        Student(){}
};

bool cmp_name(Student a, Student b){
    return a.name < b.name;
}

bool cmp_height(Student a, Student b){
    return a.height > b.height;
}

Student students[MAX_N];

int main() {
    // 여기에 코드를 작성해주세요.
    for (int i = 0; i < MAX_N; i++){
        string name;
        int height;
        double weight;

        cin >> name >> height >> weight;
        students[i] = Student(name, height, weight);
    }
    cout << fixed;
    cout.precision(1); 

    sort(students, students + MAX_N, cmp_name);

    cout << "name" << endl;
    for (int i = 0; i < MAX_N; i++){
        cout << students[i].name << " " << students[i].height << " " << students[i].weight << endl; 
    }


    sort(students, students + MAX_N, cmp_height);

    
    cout << endl << "height" << endl; 
    for (int i = 0; i < MAX_N; i++){
        cout << students[i].name << " " << students[i].height << " " << students[i].weight << endl; 
    }

    return 0;
}