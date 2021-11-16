/*
 * @Date: 2021-11-10 15:09:38
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-15 22:49:47
 * @FilePath: /a3/ece650-a3.cpp
 */

#include <fcntl.h>
#include <iostream>
#include <sys/wait.h>
#include <unistd.h>
#include <vector>

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

string a2Input()
{
	string line;
	getline(cin, line);
	return line;
}

int main(int argc, char *argv[])
{
	vector<pid_t> kids;
	pid_t pid;
	int rgentoA1[2];
	pipe(rgentoA1);
	pid = fork();
	if (pid == 0)
	{
		dup2(rgentoA1[0], STDIN_FILENO);
		close(rgentoA1[1]);
		close(rgentoA1[0]);
		a1();
	}
	if (pid < 0)
	{
		cerr << "Error: Fork error!" << endl;
		return 1;
	}
	kids.push_back(pid);
	dup2(rgentoA1[1], STDOUT_FILENO);
	close(rgentoA1[0]);
	close(rgentoA1[1]);
	rgen(argc, argv);

	for (pid_t k : kids)
	{
		int status;
		kill(k, SIGTERM);
		waitpid(k, &status, 0);
	}
}
