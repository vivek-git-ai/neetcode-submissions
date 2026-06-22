class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bucket_s = {}
        bucket_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in bucket_s:
                bucket_s[s[i]] = 1
            else:
                bucket_s[s[i]] += 1

            if t[i] not in bucket_t:
                bucket_t[t[i]] = 1
            else:
                bucket_t[t[i]] += 1  

        if bucket_s == bucket_t:
            return True
        else:
            return False              





        



        
        