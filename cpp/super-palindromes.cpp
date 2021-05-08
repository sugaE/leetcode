// https://leetcode.com/problems/super-palindromes/
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

class Solution
{
public:
  int superpalindromesInRange(string left, string right)
  {
    // vector<string> nums;
    long l = stol(left), r = stol(right), sqrtleft = long(sqrt(l)), sqrtright = long(sqrt(r));
    int nl = to_string(sqrtleft).size() / 2, nr = to_string(sqrtright).size() / 2;
    int count = 0;

    // 10^9
    // 10^4+i+10^4
    bool bigflag = false;
    long tmp;
    for (int i = pow(10, nl - 1); i < pow(10, nr + 1); i++) //9999
    {
      string cur = to_string(i);
      string rev = string(cur.rbegin(), cur.rend());
      tmp = stol(cur + rev);
      if (tmp > sqrtright)
      {
        break;
      }
      count += check(tmp, l, r);

      for (int j = 0; j <= 9 && !bigflag; j++)
      {
        tmp = cur == "0" ? j : stol(cur + to_string(j) + rev);
        if (tmp > sqrtright)
        {

          bigflag = true;
          break;
        }
        count += check(tmp, l, r);
      }
    }

    return count;
  }
  int check(long num, long l, long r)
  {
    long square = num * num;

    if (square >= l && square <= r && isPalin(to_string(square)))
    {
      cout << square << endl;
      return 1;
    }
    return 0;
  }

  bool isPalin(string num)
  {
    return num == string(num.rbegin(), num.rend());
  }
};

int main()
{

  Solution solution;

  auto res = solution.superpalindromesInRange("100000000", "100000000000000000");
  // auto res = solution.superpalindromesInRange("4", "1000");
  cout << res << endl;

  return 0;
}
