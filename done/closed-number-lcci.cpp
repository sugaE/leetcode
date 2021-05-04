// https://leetcode-cn.com/problems/closed-number-lcci/

#include <vector>
#include <stdio.h>

using namespace std;

class Solution
{
public:
  vector<int> findClosedNumbers(int num)
  {
    vector<int> res(2, -1);
    if (num < 1 || num >= __INT_MAX__)
    {
    }
    else
    {
      res[0] = getNextL(num);
      res[1] = getNextS(num);
    }

    return res;
  }

  int getNextL(int num)
  {
    int tmp = num;
    int indexOne = 0;
    int indexZero = 0;

    while (tmp > 0 && (tmp & 1) == 0)
    {
      tmp >>= 1;
      indexZero++;
    }

    while (tmp > 0 && (tmp & 1) == 1)
    {
      tmp >>= 1;
      indexOne++;
    }

    int pos = indexOne + indexZero;

    if (pos == 0 || pos == 31)
    {
      return -1;
    }

    num |= 1 << pos; // flip 0 to 1
    num &= ~((1 << pos) - 1);
    num |= (1 << (indexOne - 1)) - 1;
    return num;
  }

  int getNextS(int num)
  {
    int tmp = num;
    int indexOne = 0;
    int indexZero = 0;

    while (tmp > 0 && (tmp & 1) == 1)
    {
      tmp >>= 1;
      indexOne++;
    }

    if (tmp == 0)
    {
      return -1;
    }

    while (tmp > 0 && (tmp & 1) == 0)
    {
      tmp >>= 1;
      indexZero++;
    }

    int pos = indexOne + indexZero;

    num &= ~((1 << (pos + 1)) - 1);
    int mask = ((1 << (indexOne + 1)) - 1);
    num |= mask << (indexZero - 1);

    return num;
  }
};

int main()
{

  Solution solution;

  // 2147483645 2147483647 67 34 2 1
  solution.findClosedNumbers(34);

  return 0;
}
