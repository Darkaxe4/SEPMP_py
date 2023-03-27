#include<iostream>

using namespace std;

void without_arr(int current_iteration)
{
    int curval;
    cin >> curval;
    if (current_iteration == 1)
    {
        cout << curval << " ";
    }
    else
    {
        without_arr(current_iteration-1);
        cout << curval << " ";
    }
}


int main()
{
    int num;
    cin >> num;
    without_arr(num);
    return 0;
}