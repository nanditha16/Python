# Given a list of accounts where each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name,
# and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely 
# belong to the same person if there is some common email to both accounts. 
# Note that even if two accounts have the same name, they may belong to 
# different people as people could have the same name. A person can have 
# any number of accounts initially, but all of their accounts definitely 
# have the same name.

# After merging the accounts, return the accounts in the following format: 
# the first element of each account is the name, and the rest of the elements 
# are emails in sorted order. The accounts themselves can be returned 
# in any order.

# Constraints:
#     1 <= accounts.length <= 1000
#     2 <= accounts[i].length <= 10
#     1 <= accounts[i][j].length <= 30
#     accounts[i][0] consists of English letters.
#     accounts[i][j] (for j > 0) is a valid email.

# Time Complexity: O(N × α(N) + M log M)
#     Union-Find operations: O(N × α(N))
#     Sorting emails: O(M log M)
#     Total: O(N × α(N) + M log M)
# Space Complexity: O(N) for parent map, email-to-name map, and groupings
    
# Example:
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
#                    ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
#                    ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
#                    ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
#                    ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
#          ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
#          ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
#          ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
#          ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 
from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Initialize parent and map emails to names
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        # Step 2: Group emails by root parent
        groups = defaultdict(set)
        for email in parent:
            root = find(email)
            groups[root].add(email)

        # Step 3: Format result
        return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]

