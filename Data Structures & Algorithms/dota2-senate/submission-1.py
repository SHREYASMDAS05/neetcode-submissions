class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        R , D  = deque() , deque()
        for i , c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        while D and R:
            r_turn = R.popleft()
            d_turn = D.popleft()
            if r_turn < d_turn:
                R.append(r_turn + len(senate))
            else:
                D.append(d_turn + len(senate))



        return 'Radiant' if R else 'Dire'