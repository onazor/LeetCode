class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        times = []

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                initial_land = landStartTime[i] + landDuration[i]
                if initial_land > waterStartTime[j]:
                    total_time = initial_land + waterDuration[j]
                else:
                    total_time = waterStartTime[j]  + waterDuration[j]

                times.append(total_time)
        
        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                initial_water = waterStartTime[i] + waterDuration[i]
                if initial_water > landStartTime[j]:
                    total_time = initial_water + landDuration[j]
                else:
                    total_time = landStartTime[j] + landDuration[j]

                times.append(total_time)
        
        return min(times)