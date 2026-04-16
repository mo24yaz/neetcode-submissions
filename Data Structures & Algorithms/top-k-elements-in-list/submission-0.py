class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] = counts[n] + 1

        sortedCounts = (sorted(counts.items(), key=lambda x: x[1], reverse=True))
        newList = []

        for i in range(k):
            newList.append(sortedCounts[i][0])

        return newList