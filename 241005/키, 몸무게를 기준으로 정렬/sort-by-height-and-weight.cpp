#include <iostream>
#include <vector> 
#include <algorithm>

using namespace std;

#define MAX_N 10

class Person{
    public:
        string name;
        int height;
        double weight;
        Person(string name, int height, double weight){
            this->name = name;
            this->height = height;
            this->weight = weight;
        }
        Person(){}
};

vector<Person> persons; 
int n; 

bool comp(Person a, Person b){
    
    if(a.height != b.height)
        return a.height < b.height;
    
    return a.weight > b.weight; 
}


int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n;
    for (int i = 0; i < n; i++){
        string name;
        int height;
        double weight;

        cin >> name >> height >> weight ;

        persons.push_back(Person(name, height, weight));
    }
    sort(persons.begin(), persons.end(), comp);

    for (int i = 0; i < n; i++){
        cout << persons[i].name << " " << persons[i].height << " " << persons[i].weight << endl;
    }

    return 0;

    }