/*
 * @Date: 2021-11-10 15:09:38
 * @LastEditors: Kunyang Xie
 * @LastEditTime: 2021-11-18 14:46:04
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

void a2Input()
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
}

int main(int argc, char *argv[])
{
	vector<pid_t> kids;

	int rgentoA1[2];
	pipe(rgentoA1);
	int A1toA2[2];
	pipe(A1toA2);
	int inputtoA2[2];
	pipe(inputtoA2);

	pid_t pid = fork();

	if (pid == 0)
	{
		dup2(rgentoA1[0], STDIN_FILENO);
		close(rgentoA1[0]);
		close(rgentoA1[1]);
		a1();
	}
	else if (pid < 0)
	{
		cerr << "Error: Could not fork!" << endl;
		return 1;
	}

	dup2(rgentoA1[1], STDOUT_FILENO);
	close(rgentoA1[0]);
	close(rgentoA1[1]);
	rgen(argc, argv);
	int status;
	wait(&status);
	return 0;
}
