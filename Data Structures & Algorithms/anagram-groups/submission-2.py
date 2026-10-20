class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_letters = sorted(word)
            key = "".join(sorted_letters)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
                
        return list(groups.values())