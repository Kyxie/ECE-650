#include <fstream>
#include <iostream>
#include <string>
#include <unistd.h>
#include <vector>
const int A = 2;  // Attempt times

using namespace std;

int ks = 10;  // Street number
int kn = 5;	  // Segment number
int kl = 5;	  // Wait time
int kc = 20;  // Cordination range

struct Street
{
	string streetName;
	vector<int> cordx;
	vector<int> cordy;
};

vector<struct Street> Map;

void assign(string line)
{
	string s = "-s ";
	string n = "-n ";
	string l = "-l ";
	string c = "-c ";
	int ps = line.find(s);	// ps is the start index
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

int unRandGen(int min, int max)	 // Generate positive random number
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

int randGen(int c)	// Generate positive and negative random number
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

bool noSamePointInStreet(int x, int y, vector<int> first, vector<int> second)
{
	// If has same point, return 0
	bool notIn = true;
	for (int i = 0; i < first.size(); i++)
	{
		if (x == first[i] && y == second[i])
			notIn = false;
	}
	return notIn;
}

bool noCrossInStreet(int x, int y, vector<int> first, vector<int> second)
{
	// If has cross, return 0
	bool notCross = true;
	for (int i = 1; i < first.size() - 1; i++)
	{
		int end1x = first[i - 1];
		int end1y = second[i - 1];
		int end2x = first[i];
		int end2y = second[i];
		int lastx = first.back();
		int lasty = second.back();
		if ((((end1x - end2x) * (lasty - y) - (end1y - end2y) * (lastx - x)) < 0.01) &&
			(((end1x - end2x) * (lasty - y) - (end1y - end2y) * (lastx - x)) > -0.01))
			// Parallel
			continue;
		else
		{
			double px = ((end1x * end2y - end1y * end2x) * (lastx - x) - (end1x - end2x) * (lastx * y - lasty * x)) /
						((end1x - end2x) * (lasty - y) - (end1y - end2y) * (lastx - x));
			double py = ((end1x * end2y - end1y * end2x) * (lasty - y) - (end1y - end2y) * (lastx * y - lasty * x)) /
						((end1x - end2x) * (lasty - y) - (end1y - end2y) * (lastx - x));
			if ((min(end1x, end2x) <= px && px <= max(end1x, end2x)) &&
				(min(end1y, end2y) <= py && py <= max(end1y, end2y)))
				notCross = false;
		}
	}
	return notCross;
}

bool noOverlapInStreet(int x, int y, vector<int> first, vector<int> second)
{
	// If has overlap, return 0
	bool notLap = true;
	int end1x = first[first.size() - 1];  // Last point
	int end1y = second[second.size() - 1];
	int end2x = first[first.size() - 2];  // Second last point
	int end2y = second[second.size() - 2];
	if (((x - end1x) * (end2y - end1y) - (y - end1y) * (end2x - end1x) < 0.01) &&
		((x - end1x) * (end2y - end1y) - (y - end1y) * (end2x - end1x) > -0.01))
	{
		// 3 points in a line
		if ((min(x, end2x) <= end1x && end1x <= max(x, end2x)) && (min(y, end2y) <= end1y && end1y <= max(y, end2y)))
			// Only the last point in middle is available
			notLap = true;
		else
			notLap = false;
	}
	return notLap;
}

bool noOverlapInMap(int x, int y, int lastx, int lasty, vector<struct Street> Map)
{
	// If has overlap, return 0
	bool notLap = true;
	for (int i = 0; i < Map.size(); i++)
	{
		for (int j = 1; j < Map[i].cordx.size(); j++)
		{
			int end1x = Map[i].cordx[j - 1];
			int end1y = Map[i].cordy[j - 1];
			int end2x = Map[i].cordx[j];
			int end2y = Map[i].cordy[j];
			if ((((end1x - end2x) * (lasty - y) - (end1y - end2y) * (lastx - x)) < 0.01) &&
				(((end1x - end2x) * (lasty - y) - (end1y - end2y) * (lastx - x)) > -0.01))
			{
				// Parallel
				if (((x - end1x) * (end2y - end1y) - (y - end1y) * (end2x - end1x) < 0.01) &&
						((x - end1x) * (end2y - end1y) - (y - end1y) * (end2x - end1x) > -0.01) ||
					((lastx - end1x) * (end2y - end1y) - (lasty - end1y) * (end2x - end1x) < 0.01) &&
						((lastx - end1x) * (end2y - end1y) - (lasty - end1y) * (end2x - end1x) > -0.01))
				{
					// 3 points in a line
					if (((x > max(end1x, end2x) && y > max(end1y, end2y)) ||
						 (x < min(end1x, end2x) && y < min(end1y, end2y))) &&
						((lastx > max(end1x, end2x) && lasty > max(end1y, end2y)) ||
						 (lastx < min(end1x, end2x) && lasty < min(end1y, end2y))))
					{
						// If (lastx, lasty) and (x, y) are both out of the range of end1 and end2
						continue;
					}
					else
					{
						notLap = false;
						return notLap;
					}
				}
				else
					continue;
			}
			else
				continue;
		}
	}
	return notLap;
}

void generateMap()
{
	int streetNum = unRandGen(2, ks);  // streetNum [2, ks]
	for (int i = 0; i < streetNum; i++)
	{
		struct Street street;
		string streetName = "Street" + to_string(i + 1);
		street.streetName = streetName;
		int lineSegNum = unRandGen(1, kn);	// lineSegNum [1, kn]
		vector<int> first;					// Be stored
		vector<int> second;
		int j = 0;
		while (j < lineSegNum)
		{
			int x = randGen(kc);  // New points
			int y = randGen(kc);
			if (Map.size() < 1)	 // 0 street
			{
				if (first.size() == 0)	// Nothing in the street
				{
					first.push_back(x);
					second.push_back(y);
					j++;
					continue;
				}
				else if (first.size() == 1)	 // street already has 1 segment
				{
					if (noSamePointInStreet(x, y, first, second) == 1)
					{
						first.push_back(x);
						second.push_back(y);
						j++;
						continue;
					}
					else
						continue;
				}
				else if (first.size() == 2)	 // street already has 2 segments
				{
					if (noSamePointInStreet(x, y, first, second) == 1 && noOverlapInStreet(x, y, first, second) == 1)
					{
						first.push_back(x);
						second.push_back(y);
						j++;
						continue;
					}
					else
						continue;
				}
				else  // street already has 3 or more segments
				{
					if (noSamePointInStreet(x, y, first, second) == 1 && noOverlapInStreet(x, y, first, second) == 1 &&
						noCrossInStreet(x, y, first, second) == 1)
					{
						first.push_back(x);
						second.push_back(y);
						j++;
						continue;
					}
					else
						continue;
				}
			}
			else  // More or equal to 2 streets
			{
				if (first.size() == 0)	// Nothing in the street
				{
					first.push_back(x);
					second.push_back(y);
					j++;
					continue;
				}
				else if (first.size() == 1)	 // street already has 1 segment
				{
					if (noOverlapInMap(x, y, first.back(), second.back(), Map) == 1 &&
						noSamePointInStreet(x, y, first, second) == 1)
					{
						first.push_back(x);
						second.push_back(y);
						j++;
						continue;
					}
					else
						continue;
				}
				else if (first.size() == 2)	 // street already has 2 segments
				{
					if (noOverlapInMap(x, y, first.back(), second.back(), Map) == 1 &&
						noSamePointInStreet(x, y, first, second) == 1 && noOverlapInStreet(x, y, first, second) == 1)
					{
						first.push_back(x);
						second.push_back(y);
						j++;
						continue;
					}
					else
						continue;
				}
				else  // street already has 3 or more segments
				{
					if (noOverlapInMap(x, y, first.back(), second.back(), Map) == 1 &&
						noSamePointInStreet(x, y, first, second) == 1 && noOverlapInStreet(x, y, first, second) == 1 &&
						noCrossInStreet(x, y, first, second) == 1)
					{
						first.push_back(x);
						second.push_back(y);
						j++;
						continue;
					}
					else
						continue;
				}
			}
		}
		street.cordx = first;
		street.cordy = second;
		Map.push_back(street);
	}
}

void printCommand(vector<struct Street> Map)
{
	cout << "clr" << endl;
	for (int i = 0; i < Map.size(); i++)
	{
		cout << "add \"" << Map[i].streetName << "\" ";
		for (int j = 0; j < Map[i].cordx.size() - 1; j++)
			cout << "(" << Map[i].cordx[j] << "," << Map[i].cordy[j] << ") ";
		cout << "(" << Map[i].cordx.back() << "," << Map[i].cordy.back() << ")" << endl;
	}
	cout << "gg" << endl;
}

int main()
{
	string line;
	getline(cin, line);
	assign(line);
	for (int i = 0; i <= A; i++)
	{
		if (i < A - 1)
		{
			int wait = unRandGen(5, kl);  // wait [5, kl]
			Map.clear();
			generateMap();
			printCommand(Map);
			sleep(wait);
		}
		else if (i == A - 1)
		{
			Map.clear();
			generateMap();
			printCommand(Map);
		}
		else
		{
			cerr << "Error: failed to generate valid input for " << A << " simultaneous attempts!" << endl;
			exit(0);
		}
	}
	return 0;
}

// -s 5 -n 4 -l 5