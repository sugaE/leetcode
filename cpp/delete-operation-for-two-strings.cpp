// https://leetcode.com/problems/delete-operation-for-two-strings/
#include <vector>
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
  int minDistance(string word1, string word2)
  {
    // int t[][] = new int[word1.size() + 1][word2.size() + 1];
    int w1 = word1.size(), w2 = word2.size();
    vector<vector<int>> t(w1 + 1, vector<int>(w2 + 1, 0));

    for (int i = 1; i <= w1; i++)
    {
      for (int j = 1; j <= w2; j++)
      {
        if (word1[i - 1] == word2[j - 1])
        {
          t[i][j] = t[i - 1][j - 1] + 1;
        }
        else
        {
          t[i][j] = max(t[i - 1][j], t[i][j - 1]);
        }
      }
    }

    return w1 + w2 - 2 * t[w1][w2];
  }
};

int main()
{

  Solution solution;

  auto res = solution.minDistance("lee", "le");
  cout << res << endl;

  return 0;
}
