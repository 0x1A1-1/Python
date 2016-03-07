ass Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        pos_sum = 0
        ans_set = set()
        need_set = set()
        for size in range(1,len(nums)+1):
            for comb in itertools.combinations(nums, size):
                sum = 0
                for i in comb:
                    sum+=i
                ans_set.add(sum)
        print(ans_set)
        for i in range(1, n+1):
            if i not in ans_set:
                need_set.add(i)
        print(need_set)
