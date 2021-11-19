/*
 * @Date: 2021-11-19 12:11:42
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-19 12:28:35
 * @FilePath: /a3/a1Output.cpp
 */

#include <iostream>

using namespace std;

int main()
{
    while (!cin.eof())
    {
        string line;
        getline(cin, line);
        if (line[0] == 'V')
        {
            cout << line << endl;
            continue;
        }
        if (line[0] == 'E')
        {
            cout << line << endl;
            break;
        }
        else
            continue;
    }
    return 0;
}