// https://leetcode.com/problems/construct-target-array-with-multiple-sums/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>

using namespace std;

class Solution
{
public:
  bool isPossible(vector<int> &target)
  {
    long sm = 0;
    int x = 0;
    priority_queue<int> pq(target.begin(), target.end());
    for (int a : target)
    {
      sm += a;
    }

    while (1)
    {
      x = pq.top();
      pq.pop();
      sm -= x;
      if (x == 1 || sm == 1)
        return true;
      if (x < sm || sm < 1 || x % sm == 0)
        return false;
      x %= sm;
      sm += x;
      pq.push(x);
    }
  };
};

int main()
{

  Solution solution;
  // vector<int> t{8, 5};
  // vector<int> t{1, 1, 1, 2};
  // vector<int> t{1, 1, 2};
  vector<int> t{1, 1000000000};

  auto res = solution.isPossible(t);
  // auto res = solution.superpalindromesInRange("4", "1000");
  cout << res << endl;

  return 0;
}
