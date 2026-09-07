class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for src, targ, time in times:
            adj_list[src].append([targ , time])

        priority_que = [[0,k]] #time_to_reach , node_src as priority q need to be inorder of time 
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        while priority_que:
            time , node = heapq.heappop(priority_que)
            if dist[node] < time:
                continue

            for child ,extra_time in adj_list[node]:
                new_time = time + extra_time
                if new_time < dist[child]:
                    dist[child] = new_time
                    heapq.heappush(priority_que , [new_time, child])
        ans = max(dist[1:])

        return -1 if ans == float('inf') else ans
            