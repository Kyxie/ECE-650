/*
 * @Date: 2021-11-10 15:09:38
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-14 16:53:42
 * @FilePath: /a3/ece650-a3.cpp
 */

#include <iostream>
#include <unistd.h>

using namespace std;

int rgen()
{
	char *argv[2] = {"rgen", NULL};
	return execv("rgen", argv);
}

int a1()
{
	char *argv[3] = {"python", "ece650-a1.py", NULL};
	return execvp("python", argv);
}

int a2()
{
	char *argv[2] = {"ece650-a2.cpp", NULL};
	return execv("ece650-a2.cpp", argv);
}

int main(int argc, char **argv)
{
	a2();
	return 0;
}