class Unionfind:
    def __init__(self ,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self ,x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]

        return x
    def union(self,x1 , x2):
        p1 , p2 = self.find(x1) , self.find(x2)
        if p1 == p2 :
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Unionfind(len(accounts))
        emailtoacc = {} #email to account index

        for i , a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoacc:
                    uf.union(i , emailtoacc[e])
                else:
                    emailtoacc[e] = i

        emailgroup = defaultdict(list)#index of acc -> email
        for e , i in emailtoacc.items():
            leader = uf.find(i)
            emailgroup[leader].append(e)

        res = []
        for i , e in emailgroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailgroup[i]))

        return res
        