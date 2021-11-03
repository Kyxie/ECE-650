#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int VNum;
vector <int> first;
vector <int> second;

int V(string line)
{
    // vertex: int type
    // vertice: string type
    int vertex;
    string vertice;
    for(int i = 2; i <= line.length(); i++)
        vertice[i - 2] = line[i];
    vertex = atoi(vertice.c_str());
    return vertex;
}


bool checkE(vector <int> side)
{
    bool EOK = true;
    for(int i = 0; i < side.size(); i++)
    {
        if(side[i] > VNum)
        {
            EOK = false;
            break;
        }
    }
    return EOK;
}


bool checks(int start, int end)
{
    bool sOK = true;
    if(start > VNum || end > VNum)
        sOK = false;
    return sOK;
}


void find(int start, int end)
{
    cout << "s is ok" << endl;
}


int main()
{
    while (!cin.eof())
    {
        string line;
        getline(cin, line); 
        if(line[0] == 'V')
        {
            first.clear();
            second.clear();
            VNum = V(line);
        }
        else if(line[0] == 'E')
        {
            for(int i = 3; i <= line.length(); i++)
            {
                if(line[i] == '<')
                {
                    char number[5] = {0};
                    for(int j = 0; line[i + j + 1] != ','; j++)
                        number[j] = line[i + j + 1];
                    int number_int = atoi(number);
                    first.push_back(number_int);
                    continue;
                }
                if(line[i] == '>')
                {
                    int j;
                    char number[5] = {0};
                    char number_inv[5] = {0};
                    for(j = 0; line[i - j - 1] != ','; j++)
                        number[j] = line[i - j - 1];
                    for(int k = 0; k <= j; k++)
                        number_inv[k] = number[j - k - 1];
                    int number_int = atoi(number_inv);
                    second.push_back(number_int);
                    continue;
                }
            }
            if(checkE(first) == false || checkE(second) == false)
            {
                first.clear();
                second.clear();
                cout << "Error: Point in E is out of the range of point in V!" << endl;
                continue;
            }
        }
        else if(line[0] == 's')
        {
            int start;
            int end;
            char number[5] = {0};
            int i;
            for(i = 0; line[1 + i + 1] != ' '; i++)
                number[i] = line[1 + i + 1];
            start = atoi(number);
            for(int j = 0; i + j + 2 <= line.length(); j++)
                number[j] = line[i + j + 2];
            end = atoi(number);
            if(checks(start, end))
                find(start, end);
            else
            {
                cout << "Error: Point in s is out of the range of point in V!" << endl;
                continue;
            }
        }
    }
    return 0;
}