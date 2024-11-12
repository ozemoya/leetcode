import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the graph as an adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: Initialize the min-heap and distance dictionary
        min_heap = [(0, k)]  # (time, node)
        shortest_times = {i: float('inf') for i in range(1, n + 1)}
        shortest_times[k] = 0
        
        # Step 3: Dijkstra's algorithm
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            # Skip if we already found a shorter path to this node
            if time > shortest_times[node]:
                continue
            
            # Explore the neighbors
            for neighbor, weight in graph[node]:
                new_time = time + weight
                if new_time < shortest_times[neighbor]:
                    shortest_times[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))
        
        # Step 4: Find the maximum delay time
        max_delay = max(shortest_times.values())
        return max_delay if max_delay < float('inf') else -1