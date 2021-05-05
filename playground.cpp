// https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3732/
#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;

class Solution
{
public:
  int jump(vector<int> &nums)
  {
    int sizen = nums.size();
    // vector<int> maxdis;
    int maxi = 0;
    int cur = -1;
    int count = 0;

    for (int i = 0; maxi < sizen - 1; i++)
    {
      if (i > cur)
      {
        cur = maxi;
        count++;
      }
      maxi = max(maxi, nums[i] + i);

      // maxdis.push_back(nums[i] + i);
      // maxi = maxdis[i] > maxdis[maxi] ? i : maxi;
      // if (maxdis[i] >= sizen - 1)
      // {
      //   count++;
      //   break;
      // }
    }
    // while (maxi > 0)
    // {
    //   for (int i = 0; i < maxdis.size() - 1; i++)
    //   {
    //     if (maxdis[i] >= maxi)
    //     {
    //       maxi = i;
    //       count++;
    //       break;
    //     }
    //   }
    // }
    return count;
  }
};

int main()
{

  Solution solution;

  vector<int> t = {2, 3, 1, 1, 4};
  solution.jump(t);

  vector<int> t2 = {0};
  solution.jump(t2);

  return 0;
}
