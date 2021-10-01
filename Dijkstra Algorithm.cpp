
#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 1;

vector<int> visited(maxn, 0), dist(maxn, INT_MAX);
vector<pair<int, int>> graph[maxn];

void Dijkstra()
{
    dist[1] = 0;

    multiset<pair<int, int>> ms;
    // {distance, vertex}
    ms.insert({0, 1});

    while (!ms.empty())
    {
        pair<int, int> tmp = *ms.begin();
        ms.erase(ms.begin());

        int v = tmp.second, weight = tmp.first;

        if (visited[v])
            continue;

        visited[v] = true;

        for (int u = 0; u < graph[v].size(); u++)
        {
            int vertex = graph[v][u].first, edge = graph[v][u].second;

            if (dist[v] + edge < dist[vertex])
            {
                dist[vertex] = dist[v] + edge;
                ms.insert({dist[vertex], vertex});
            }
        }
    }
}

int main()
{

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        int x, y, z;
        cin >> x >> y >> z;

        // Directed graph
        graph[x].push_back({y, z});

        // For Undirected graph
        // graph[y].push_back({x, z});
    }

    Dijkstra();

    return 0;
}
