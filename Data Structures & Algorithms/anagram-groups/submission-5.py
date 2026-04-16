# Brute Force Solution (O(n^2 * k log k))
def groupAnagrams_bruteforce(self, strs: List[str]) -> List[List[str]]:
    res = []
    visited = set()
    
    for i in range(len(strs)):
        if strs[i] not in visited:
            newList = []

            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    newList.append(strs[j])
                    visited.add(strs[j])

            res.append(newList)

    return res

# Optimized Solution (O(n * k log k))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        
        for s in strs:
            curr = "".join(sorted(s))

            if curr not in myDict:
                myDict[curr] = [s]
            else:
                myDict[curr].append(s)


        return list(myDict.values())