/*
 * @Date: 2021-11-10 20:32:11
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-17 16:53:21
 * @FilePath: /a3/ece650-a2.cpp
 */

#include <iostream>
#include <vector>

#define INF 100000

using std::cerr;
using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

int VNum;
vector<int> first;
vector<int> second;

int V(string line)
{
	// vertex: int type
	// vertice: string type
	int vertex;
	string vertice;
	for (int i = 2; i <= line.length(); i++)
		vertice[i - 2] = line[i];
	vertex = atoi(vertice.c_str());
	return vertex;
}

bool checkE(vector<int> side)
{
	bool EOK = true;
	for (int i = 0; i < side.size(); i++)
	{
		if (side[i] > VNum)
		{
			EOK = false;
			break;
		}
	}
	return EOK;
}

bool alreadyIn(vector<int> alreadyInputs, int key)
{
	bool alreadyIn = false;
	for (int i = 0; i < alreadyInputs.size(); i++)
	{
		if (key == alreadyInputs[i])
		{
			alreadyIn = true;
			break;
		}
	}
	return alreadyIn;
}

vector<int> findNumber(vector<int> first, vector<int> second)
{
	bool boolAlreadyIn = false;
	vector<int> set;
	for (int i = 0; i < first.size(); i++)
	{
		boolAlreadyIn = alreadyIn(set, first[i]);
		if (boolAlreadyIn)
			continue;
		else
			set.push_back(first[i]);
	}
	for (int i = 0; i < first.size(); i++)
	{
		boolAlreadyIn = alreadyIn(set, second[i]);
		if (boolAlreadyIn)
			continue;
		else
			set.push_back(second[i]);
	}
	return set;
}

int checks(int start, int end)
{
	// sOK = 1 means good
	// sOK = 2 means s out of V
	// sOK = 3 means no route
	int sOK = 1;
	if (start > VNum || end > VNum)
		sOK = 2;
	vector<int> set = findNumber(first, second);
	bool noStart = alreadyIn(set, start);
	bool noEnd = alreadyIn(set, end);
	if (start <= VNum && end <= VNum && (noStart == false || noEnd == false))
		sOK = 3;
	return sOK;
}

vector<int> find(int start, int end)
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
	for (int i = 0; i < VNum - 1; i++)
	{
		for (int j = 0; j < first.size(); j++)
		{
			int from = first[j];
			int to = second[j];
			if (distance[from] > distance[to] + 1)
			{
				distance[from] = distance[to] + 1;
				previous[from] = to;
			}
			if (distance[to] > distance[from] + 1)
			{
				distance[to] = distance[from] + 1;
				previous[to] = from;
			}
		}
	}

	// for(int i = 1; i <= VNum; i++)
	//     cout << "dist[" << i << "] = " << distance[i] << endl;
	// cout << "**************************" << endl;
	// for(int i = 1; i <= VNum; i++)
	//     cout << "prev[" << i << "] = " << previous[i] << endl;

	vector<int> route;
	route.push_back(end);
	while (route.back() != start)
		if (previous[route.back()] <= VNum)
			route.push_back(previous[route.back()]);
		else
			break;
	return route;
}

void print(vector<int> route)
{
	for (int i = route.size() - 1; i >= 0; i--)
	{
		if (i != 0)
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
		if (line[0] == 'V')
		{
			cout << line << endl;
			first.clear();
			second.clear();
			VNum = V(line);
		}
		else if (line[0] == 'E')
		{
			cout << line << endl;
			for (int i = 3; i <= line.length(); i++)
			{
				if (line[i] == '<')
				{
					char number[5] = {0};
					for (int j = 0; line[i + j + 1] != ','; j++)
						number[j] = line[i + j + 1];
					int number_int = atoi(number);
					first.push_back(number_int);
					continue;
				}
				if (line[i] == '>')
				{
					int j;
					char number[5] = {0};
					char number_inv[5] = {0};
					for (j = 0; line[i - j - 1] != ','; j++)
						number[j] = line[i - j - 1];
					for (int k = 0; k <= j; k++)
						number_inv[k] = number[j - k - 1];
					int number_int = atoi(number_inv);
					second.push_back(number_int);
					continue;
				}
			}
			if (checkE(first) == false || checkE(second) == false)
			{
				first.clear();
				second.clear();
				cerr << "Error: Point in E is out of the range of point in V!" << endl;
				continue;
			}
		}
		else if (line[0] == 's')
		{
			int start;
			int end;
			char number[5] = {0};
			int i;
			for (i = 0; line[1 + i + 1] != ' '; i++)
				number[i] = line[1 + i + 1];
			start = atoi(number);
			for (int j = 0; i + j + 2 <= line.length(); j++)
				number[j] = line[i + j + 2];
			end = atoi(number);
			if (checks(start, end) == 1)
			{
				vector<int> route = find(start, end);
				if (route.size() > 1)
					print(route);
				else
					cerr << "Error: No path exists!" << endl;
				continue;
			}
			else if (checks(start, end) == 2)
			{
				cerr << "Error: Point in s must be in the range of E and V!" << endl;
				continue;
			}
			else
			{
				cout << "Error: No path exists!" << endl;
				continue;
			}
		}
	}
	return 0;
}

// V 15
// E {<2,6>,<2,8>,<2,5>,<6,5>,<5,8>,<6,10>,<10,8>}
// s 2 10
