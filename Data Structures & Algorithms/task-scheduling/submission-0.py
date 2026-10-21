class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0)+ 1

        max_count = max(counts.values())
        
        num_max_count = 0
        for count in counts.values():
            if count == max_count:
                num_max_count +=1
        
        frame = (max_count-1) * (n+1) + num_max_count
        return max(frame, len(tasks))
        









