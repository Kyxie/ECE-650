#include <iostream>
#include <vector>

#define INF 100000

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


bool alreadyIn(vector <int> alreadyInputs, int key)
{
    bool alreadyIn = false;
    for(int i = 0; i < alreadyInputs.size(); i++)
    {
        if(key == alreadyInputs[i])
        {
            alreadyIn = true;
            break;
        }
    }
    return alreadyIn;
}


vector <int> findNumber(vector <int> first, vector <int> second)
{
    bool boolAlreadyIn = false;
    vector <int> set;
    for(int i = 0; i < first.size(); i++)
    {
        boolAlreadyIn = alreadyIn(set, first[i]);
        if(boolAlreadyIn)
            continue;
        else
            set.push_back(first[i]);
    }
    for(int i = 0; i < first.size(); i++)
    {
        boolAlreadyIn = alreadyIn(set, second[i]);
        if(boolAlreadyIn)
            continue;
        else
            set.push_back(second[i]);
    }
    return set;
}


bool checks(int start, int end)
{
    bool sOK = true;
    if(start > VNum || end > VNum)
        sOK = false;
    vector <int> set = findNumber(first, second);
    bool noStart = alreadyIn(set, start);
    bool noEnd = alreadyIn(set, end);
    if(noStart == false || noEnd == false)
        sOK = false;
    return sOK;
}


vector <int> find(int start, int end)
{
    int distance[50];
    int previous[50];
    for (int i = 1; i <= VNum; i++)
    {
        previous[i] = INF;
        if (i == start)
            distance[i] = 0;
        else
            distance[i] = INF;
    }
    for(int i = 0; i < VNum - 1; i++)
    {
        for(int j = 0; j < first.size(); j++)
        {
            int from = first[j];
            int to = second[j];
            if(distance[from] > distance[to] + 1)
            {
                distance[from] = distance[to] + 1;
                previous[from] = to;
            }
            if(distance[to] > distance[from] + 1)
            {
                distance[to] = distance[from] + 1;
                previous[to] = from;
            }
        }
    }
    vector <int> route;
    route.push_back(end);
    while(route.back() != start)
        route.push_back(previous[route.back()]);
    return route;
}


void print(vector <int> route)
{
    for(int i = route.size() - 1; i >= 0; i--)
    {
        if(i != 0)
            cout << route[i] << '-';
        else
            cout << route[i];
    }
    cout << endl;
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
            {
                vector <int> route = find(start, end);
                print(route);
                continue;
            }
            else
            {
                cout << "Error: Point in s must be in the range of E and V!" << endl;
                continue;
            }
        }
    }
    return 0;
}