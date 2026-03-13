import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        workers_heap = []
        for base_time in workerTimes:
            next_total_time = base_time
            current_time_spent = 0
            next_chunk_number = 1
            workers_heap.append((next_total_time, current_time_spent, base_time, next_chunk_number))

        heapq.heapify(workers_heap)
        print(workers_heap)

        for _ in range(mountainHeight):
            lowest = heapq.heappop(workers_heap)
            current_time_spent = lowest[0]
            next_chunk_number = lowest[3] + 1
            next_total_time = current_time_spent + (lowest[2]*next_chunk_number)
            heapq.heappush(workers_heap, tuple((next_total_time, current_time_spent, lowest[2], next_chunk_number)))
        return max(out[1] for out in workers_heap)