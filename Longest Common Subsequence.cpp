
// Longest Common Subsequence
// Time Complexity O(N*N)

#include <bits/stdc++.h>
using namespace std;

const int maxn = 100;
int dp[maxn][maxn];

int FindLcsLength(string a, string b)
{
    int n = a.length(), m = b.length();

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= m; j++)
        {
            if (i == 0 || j == 0)
                dp[i][j] = 0;

            else if (a[i - 1] == b[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;

            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    return dp[n][m];
}

string FindLcs(string a, string b, int len)
{
    int n = a.length(), m = b.length();
    int i = n, j = m;

    string lcs = "";

    while (i > 0 && j > 0)
    {
        if (a[i - 1] == b[j - 1])
        {
            lcs.push_back(a[i]);
            i--, j--;
        }

        else if (dp[i - 1][j] >= dp[i][j - 1])
            i--;

        else
            j--;
    }

    reverse(lcs.begin(), lcs.end());

    return lcs;
}

int main()
{
    string a = "abcbc";
    string b = "cbcba";

    memset(dp, 0, sizeof(dp));

    int len = FindLcsLength(a, b);

    string lcs = FindLcs(a, b, len);

    cout << "Length of Longest Common Subsequence : " << len << "\n";
    cout << "Longest Common Subsequence is : " << lcs << "\n";

    return 0;
}
