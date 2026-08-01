class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l , r = 0 , len(people) -1
        boat = 0
        while l <= r:
            rem = limit - people[r]
            r-=1
            boat +=1
            if l<=r and people[l] <= rem:
                l+=1
            
        return boat


            


        