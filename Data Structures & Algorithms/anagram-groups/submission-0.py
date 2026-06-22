class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        grouped_anagrams = []
        bucket = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in bucket:
                bucket[key] = [word]
            else:
                bucket[key].append(word)

        return list(bucket.values())     


        