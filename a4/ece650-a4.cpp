/*
 * @Date: 2021-11-26 15:39:46
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-28 15:11:51
 * @FilePath: /k47xie/a4/ece650-a4.cpp
 */

#include "minisat/core/Solver.h"
#include "minisat/core/SolverTypes.h"
#include <iostream>
#include <memory>
#include <vector>

using namespace std;

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

void assign(void)
{
	while (!cin.eof())
	{
		string line;
		getline(cin, line);
		if (line[0] == 'V')
		{
			first.clear();
			second.clear();
			VNum = V(line);
		}
		else if (line[0] == 'E')
		{
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
			break;
		}
	}
}

int main(void)
{
	assign();

	return 0;
}
