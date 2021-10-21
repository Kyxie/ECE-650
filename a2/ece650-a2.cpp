#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    while (!std::cin.eof())
    {
        char line[50];
        cin >> line;
        cout << "Input is " << line << endl;
    }
}