/*
 * @Date: 2021-11-26 15:39:46
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-12-04 18:54:22
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

vector<int> transform(vector<int> first, vector<int> second)
{
	vector<int> edge;
	for (int i = 0; i < first.size(); i++)
	{
		edge.push_back(first[i]);
		edge.push_back(second[i]);
	}
	return edge;
}

vector<int> SAT(vector<int> edge)
{
	unique_ptr<Minisat::Solver> solver(new Minisat::Solver());
	int Vk = 1;
	vector<int> vertex_cover;
	while (Vk <= VNum)
	{
		Minisat::Lit x[VNum][Vk];
		for (int i = 1; i <= VNum; i++)
		{
			for (int j = 1; j <= Vk; j++)
				x[i][j] = Minisat::mkLit(solver->newVar());
		}
		// First clause
		for (int i = 1; i <= Vk; i++)
		{
			Minisat::vec<Minisat::Lit> literals;
			for (int j = 1; j <= VNum; j++)
				literals.push(x[j][i]);
			solver->addClause(literals);
			// Third clause
			for (int j = 0; j < VNum; j++)
			{
				for (int k = j + 1; k < VNum; k++)
					solver->addClause(~literals[j], ~literals[k]);
			}
		}
		// Second clause
		for (int i = 1; i <= VNum; i++)
		{
			for (int j = 1; j <= Vk; j++)
			{
				for (int k = j + 1; k <= Vk; k++)
					solver->addClause(~x[i][j], ~x[i][k]);
			}
		}
		// Fourth clause
		int front;
		int back;
		for (size_t i = 0; i < edge.size() - 1; i = i + 2)
		{
			front = edge[i];
			back = edge[i + 1];
			Minisat::vec<Minisat::Lit> cover;
			for (int j = 1; j <= Vk; j++)
			{
				cover.push(x[front][j]);
				cover.push(x[back][j]);
			}
			solver->addClause(cover);
		}
		bool res = solver->solve();
		int count;
		if (res)
		{
			for (int i = 1; i <= VNum; i++)
			{
				for (int j = 1; j <= Vk; j++)
				{
					count = Minisat::toInt(solver->modelValue(x[i][j]));
					if (count == 0)
						vertex_cover.push_back(i);
				}
			}
			return vertex_cover;
		}
		Vk++;
		solver.reset(new Minisat::Solver());
	}
	return vertex_cover;
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
			vector<int> edge = transform(first, second);
			if (edge.empty())
				cout << endl;
			else
			{
				vector<int> vertex_cover = SAT(edge);
				for (size_t i = 0; i < vertex_cover.size(); i++)
					cout << vertex_cover[i] << ' ';
				cout << endl;
			}
		}
	}
}

int main(void)
{
	assign();
	return 0;
}
