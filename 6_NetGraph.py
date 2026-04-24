import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Sample data (user connections)
data = {
    'User1': ['A','A','B','C','D','E'],
    'User2': ['B','C','D','D','B','A']
}
df = pd.DataFrame(data)

# Create graph
G = nx.from_pandas_edgelist(df, 'User1', 'User2')

# Influence (degree centrality)
print("Influence (Degree Centrality):")
print(nx.degree_centrality(G))

# Community detection (simple)
from networkx.algorithms.community import greedy_modularity_communities
communities = list(greedy_modularity_communities(G))

print("\nCommunities:")
for i, c in enumerate(communities):
    print("Community", i+1, ":", list(c))

# Draw graph
nx.draw(G, with_labels=True)
plt.show()