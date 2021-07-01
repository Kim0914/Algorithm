#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<pair<int, int>> v;
    int sum = 0;
    int max = 0;
    for(int i=0; i<10; i++){
        int off_num = 0;
        int on_num = 0;
        cin >> off_num >> on_num;
        // v.push_back(make_pair(off_num, on_num));
        sum = sum - off_num + on_num;
        if(sum >= max){
            max = sum;
        }
    }
    cout << max;
}