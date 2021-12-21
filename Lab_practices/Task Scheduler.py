from typing import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size = len(tasks)
        if(size==0):
            return None
        if(n==0):
            return size
        count = Counter(tasks)
        lst_dic = dict(count)
        most_common = count.most_common(1)[-1] if count else None
        if most_common is None:
            return size
    
        common_num = most_common[1]-1
        idle = common_num * n
        lst_dic.pop(most_common[0])
        
        for key, value in lst_dic.items():
            idle -= min(value, common_num)
            
        if idle < 0:
            return len(tasks)
        
        return len(tasks) + idle
        