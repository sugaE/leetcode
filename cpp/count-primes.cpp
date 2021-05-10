// https://leetcode.com/problems/count-primes/
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
  int countPrimes(int n)
  {
    int countn = 0;
    int tomaru = (int)sqrtl(n);
    vector<bool> marks(n, false);
    for (int i = 2; i <= tomaru; i++)
    {
      if (!marks[i])
      {
        countn++;
        for (int j = i; i * j < n; j++)
        {
          // if (marks[j] % i == 0)
          // {
          marks[j * i] = true;
          // }
        }
      }
    }
    for (int i = tomaru + 1; i < n; i++)
    {
      if (!marks[i])
      {
        countn++;
      }
    }
    return countn;
  }
};

int main()
{

  Solution solution;

  // auto res = solution.countPrimes(5000000);
  auto res = solution.countPrimes(2);
  // auto res = solution.countPrimes(0);
  // auto res = solution.countPrimes(10);
  cout << res << endl;

  return 0;
}
