
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> g[100005], ans, visited(100005);

void dfs(int v)
{
    visited[v] = true;

    for (int u : g[v])
        if (!visited[u])
            dfs(u);

    ans.push_back(v);
}

void top_sort()
{
    ans.clear();

    for (int i = 0; i < n; i++)
        if (!visited[i])
            dfs(i);

    reverse(ans.begin(), ans.end());
}

int main()
{
    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;

        x--, y--;
        g[x].push_back(y);
    }

    top_sort();

    for (int i : ans)
        cout << i + 1 << " ";
    cout << "\n";

    return 0;
}
