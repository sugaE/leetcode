// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
  int maxScore(const vector<int> &cardPoints, int k)
  {
    return 0;
  }
};

int main()
{

  Solution solution;
  vector<int> results;

  results.push_back(solution.maxScore({1, 20}, 2));
  results.push_back(solution.maxScore({1, 1000, 1}, 1));
  results.push_back(solution.maxScore({1, 79, 80, 1, 1, 1, 200, 1}, 3));

  for (auto i : results)
  {
    cout << i << endl;
  }

  return 0;
}
