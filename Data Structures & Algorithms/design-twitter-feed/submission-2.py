class Twitter:

    def __init__(self):
        self.count = 0 
        self.tweetmap = defaultdict(list) # userid -> list[count , tweetid]
        self.followmap = defaultdict(set) #userid -> followeeid
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.count , tweetId))
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
            #need to get the last posts
                index = len(self.tweetmap[followeeId]) -1
                count , tweetId = self.tweetmap[followeeId][index]
                minheap.append((count , tweetId , followeeId , index -1))

        heapq.heapify(minheap)
        while minheap and len(res) < 10:
            count , tweetId , followeeId , index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count , tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap , (count , tweetId , followeeId , index -1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
