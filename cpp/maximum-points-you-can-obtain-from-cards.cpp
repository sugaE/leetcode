// https://leetcode.com/problems/count-primes/
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
  int maxScore(const vector<int> &cardPoints, int k)
  {

    int len = cardPoints.size();
    long minsum = len - k > 0 ? INT_MAX : 0, cursum = 0, totalsum = 0;
    for (int i = 0; i < len; i++)
    {
      if (i < len - k) // || i < k
      {
        totalsum += cardPoints[i];
      }
      else
      {
        totalsum += cardPoints[i];
        cursum = cursum - cardPoints[i - (len - k)] + cardPoints[i];
        minsum = min(minsum, cursum);
      }

      if (i == len - k - 1)
      {
        minsum = totalsum;
        cursum = totalsum;
      }
    }
    return totalsum - minsum;
  }
};

int main()
{

  Solution solution;
  vector<int> results;

  // auto res = solution.countPrimes(5000000);
  results.push_back(solution.maxScore({1, 20}, 2));
  results.push_back(solution.maxScore({1, 1000, 1}, 1));
  results.push_back(solution.maxScore({1, 79, 80, 1, 1, 1, 200, 1}, 3));
  // auto res = solution.countPrimes(0);
  // auto res = solution.countPrimes(10);

  for (auto i : results)
  {
    cout << i << endl;
  }

  return 0;
}
