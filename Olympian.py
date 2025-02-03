import requests
from collections import defaultdict
def main():
    # Set up headers with JWT and content-type
    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImdpdGh1YjU2NzcwOTc2IiwiZW1haWwiOm51bGwsInByb3ZpZGVyIjoiZ2l0aHViIiwicm9sZXMiOlsiVVNFUiJdLCJleHAiOjE3Mzg0NTIyNzAuNDUxLCJpYXQiOjE3MzgzNjU4NzB9.-2SnqEsRyOV8kPgES3f8lcU7aCvIUt_dg48UjhFRLyU",
        "Content-Type": "application/json"
    }
    # Get input data
    response = requests.get("https://adonix.hackillinois.org/registration/challenge/", headers=headers)
    data = response.json()
    alliances = data.get('alliances', [])
    people = data.get('people', {})

    # Initialize Union-Find
    parent = {name: name for name in people}
    rank = {name: 1 for name in people}

    def find(name):
        if parent[name] != name:
            parent[name] = find(parent[name])  # Path compression
        return parent[name]

    def union(name1, name2):
        root1 = find(name1)
        root2 = find(name2)
        if root1 != root2:
            # Union by rank
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]

    # Process all alliances
    for u, v in alliances:
        union(u, v)
    # Calculate sums for each component
    sums = defaultdict(int)
    for name in people:
        root = find(name)
        sums[root] += people[name]

    max_divine_power = max(sums.values()) if sums else 0

    # Submit the solution
    post_data = {"solution": max_divine_power}
    post_response = requests.post(
        "https://adonix.hackillinois.org/registration/challenge/",
        headers=headers,
        json=post_data
    )

    print(post_response.text)

if __name__ == "__main__":
    main()
