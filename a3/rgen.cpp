#include <iostream>
#include <string>
#include <fstream>

using std::cerr;
using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::rand;
using std::string;

int ks = 10;
int kn = 5;
int kl = 5;
int kc = 20;

void assign(string line)
{
    string s = "-s ";
    string n = "-n ";
    string l = "-l ";
    string c = "-c ";
    int ps = line.find(s); // ps is the start index
    int pn = line.find(n);
    int pl = line.find(l);
    int pc = line.find(c);
    if (ps != string::npos)
    {
        char number[5];
        int i = 0;
        while (line[ps + 3 + i] >= '0' and line[ps + 3 + i] <= '9')
        {
            number[i] = line[ps + 3 + i];
            i++;
        }
        ks = atoi(number);
    }
    if (pn != string::npos)
    {
        char number[5];
        int i = 0;
        while (line[pn + 3 + i] >= '0' and line[pn + 3 + i] <= '9')
        {
            number[i] = line[pn + 3 + i];
            i++;
        }
        kn = atoi(number);
    }
    if (pl != string::npos)
    {
        char number[5];
        int i = 0;
        while (line[pl + 3 + i] >= '0' and line[pl + 3 + i] <= '9')
        {
            number[i] = line[pl + 3 + i];
            i++;
        }
        kl = atoi(number);
    }
    if (pc != string::npos)
    {
        char number[5];
        int i = 0;
        while (line[pc + 3 + i] >= '0' and line[pc + 3 + i] <= '9')
        {
            number[i] = line[pc + 3 + i];
            i++;
        }
        kc = atoi(number);
    }
}

int unRandGen(int min, int max) // Generate positive random number
{
    ifstream urandom("/dev/urandom");
    if (urandom.fail())
        return 1;
    char ch = 'a';
    while (1)
    {
        urandom.read(&ch, 1);
        if (min - 1 < (unsigned int)ch && (unsigned int)ch < max + 1)
            break;
    }
    urandom.close();
    return (unsigned int)ch;
}

int randGen(int c) // Generate positive and negative random number
{
    ifstream urandom("/dev/urandom");
    if (urandom.fail())
        return 1;
    char ch = 'a';
    while (true)
    {
        urandom.read(&ch, 1);
        if (-c - 1 < ch && ch < c + 1)
            break;
    }
    urandom.close();
    return ch;
}

void generateMap()
{
    int streetNum = unRandGen(2, ks); // streetNum [2, ks]
    int wait = unRandGen(5, kl);      // wait [5, kl]
    for (int i = 0; i < streetNum; i++)
    {
        int lineSeg = unRandGen(1, kn); // lineSeg [1, kn]
        int x[lineSeg] = {0};
        int y[lineSeg] = {0};
        for (int j = 0; j < lineSeg; j++)
        {
            x[j] = randGen(kc);
            y[j] = randGen(kc);
        }
    }
}

int main()
{
    string line;
    getline(cin, line);
    const int A = 25;
    assign(line);
    for (int i = 0; i <= A; i++)
    {
        if (i < A)
        {
            // cout << "clr" << endl;
            generateMap();
        }
        else
        {
            cerr << "Error: failed to generate valid input for 25 simultaneous attempts!" << endl;
            exit(0);
        }
    }
    return 0;
}