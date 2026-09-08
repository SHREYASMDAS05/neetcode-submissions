class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        self.count -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        n = len(nums)

        if n == 1:
            return True

        if 1 in nums:
            return False

        uf = UnionFind(n)

        factor_to_index = {}

        for i, num in enumerate(nums):
            x = num
            factor = 2

            while factor * factor <= x:
                if x % factor == 0:

                    # Connect this number to another number
                    # that contains the same prime factor
                    if factor in factor_to_index:
                        uf.union(i, factor_to_index[factor])
                    else:
                        factor_to_index[factor] = i

                    while x % factor == 0:
                        x //= factor

                factor += 1

            # Remaining x is a prime factor
            if x > 1:
                if x in factor_to_index:
                    uf.union(i, factor_to_index[x])
                else:
                    factor_to_index[x] = i
        return uf.count == 1
        