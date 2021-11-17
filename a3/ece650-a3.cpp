/*
 * @Date: 2021-11-10 15:09:38
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-16 21:44:16
 * @FilePath: /a3/ece650-a3.cpp
 */

#include <fcntl.h>
#include <iostream>
#include <sys/wait.h>
#include <unistd.h>
#include <vector>

using namespace std;

int rgen(int argc, char *argv[])
{
	argv[0] = (char *)"./rgen";
	execv(argv[0], argv);
	return 0;
}

int a1()
{
	char *argv[] = {(char *)"python3", (char *)"ece650-a1.py", NULL};
	execvp(argv[0], argv);
	return 0;
}

int a2()
{
	char *argv[] = {(char *)"./ece650-a2", NULL};
	execv(argv[0], argv);
	return 0;
}

int a2Input()
{
	while (!std::cin.eof())
	{
		string line;
		getline(std::cin, line);
		if (cin.eof())
			break;
		cout << line << endl;
		cout.flush();
	}
	return 0;
}

int main(int argc, char *argv[])
{
	vector<pid_t> kids;
	pid_t pid;

	int rgentoA1[2];
	pipe(rgentoA1);
	int A1toA2[2];
	pipe(A1toA2);
	int A1toA3[2];
	pipe(A1toA3);

	pid = fork();
	if (pid == 0)
	{
		dup2(rgentoA1[0], STDIN_FILENO);
		close(rgentoA1[0]);
		close(rgentoA1[1]);

		dup2(A1toA2[1], STDOUT_FILENO);
		close(A1toA2[0]);
		close(A1toA2[1]);
		return a1();
	}
	else if (pid < 0)
	{
		cerr << "Error: Could not fork!" << endl;
		return 1;
	}
	kids.push_back(pid);

	pid = fork();
	if (pid == 0)
	{
		dup2(rgentoA1[1], STDOUT_FILENO);
		close(rgentoA1[0]);
		close(rgentoA1[1]);
		return rgen(argc, argv);
	}
	else if (pid < 0)
	{
		cerr << "Error: Could not fork!" << endl;
		return 1;
	}
	kids.push_back(pid);

	pid = fork();
	if (pid == 0)
	{
		dup2(A1toA2[0], STDIN_FILENO);
		close(A1toA2[0]);
		close(A1toA2[1]);
		return a2();
	}
	else if (pid < 0)
	{
		cerr << "Error: Could not fork!" << endl;
		return 1;
	}
	kids.push_back(pid);

	pid = fork();
	if (pid == 0)
	{
		dup2(A1toA2[1], STDOUT_FILENO);
		close(A1toA2[0]);
		close(A1toA2[1]);
		return a2Input();
	}
	else if (pid < 0)
	{
		cerr << "Error: Could not fork!" << endl;
		return 1;
	}
	kids.push_back(pid);

	int status;
	waitpid(-1, &status, 0);
	for (pid_t k : kids)
	{
		int status;
		kill(k, SIGTERM);
		waitpid(k, &status, 0);
	}
	return 0;
}
