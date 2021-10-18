class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = [0] * len(intervals)
        end = [0] * len(intervals)
        count = 0
        for i in range(0, len(intervals)):
            start[i] = intervals[i][0]
            end[i] = intervals[i][1]
        start.sort()
        end.sort()
        
        startP = 0
        endP = 0
        result = 0
        while startP < len(intervals):
            if start[startP] < end[endP]:
                count += 1
                startP += 1
            else:
                count -= 1
                endP += 1
            result = max(result, count)
        
        return result
        