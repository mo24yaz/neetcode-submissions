class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        if len(s) != len(t):
            return False

        for c in s:
            s_list.append(c)

        for c in t:
            t_list.append(c)

        s_list.sort()
        t_list.sort()

        return s_list == t_list

        # return sorted(s) == sorted(t)
        # This gives the same result as the above code

       


        