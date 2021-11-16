/*
 * @Date: 2021-11-10 15:09:38
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-15 20:37:41
 * @FilePath: /a3/ece650-a3.cpp
 */
#include <iostream>
#include <unistd.h>

using namespace std;

void rgen(int argc, char *argv[])
{
	argv[0] = (char *)"./rgen";
	execv(argv[0], argv);
}

void a1()
{
	char *argv[] = {(char *)"python3", (char *)"ece650-a1.py", NULL};
	execvp(argv[0], argv);
}

void a2()
{
	char *argv[] = {(char *)"./ece650-a2", NULL};
	execv(argv[0], argv);
}

void a2Input()
{
	while (!cin.eof())
	{
		string line;
		getline(cin, line);
		cout << line << endl;
	}
}

int main(int argc, char *argv[])
{
	a1();
}