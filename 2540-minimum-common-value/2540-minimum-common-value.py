class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        dictionary = {}
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        for i in range(len(nums1)):
            if nums1[i] in dictionary:
                dictionary[nums1[i]] += 1
            else:
                dictionary[nums1[i]] = 1
        
        for j in range(len(nums2)):
            if nums2[j] in dictionary:
                dictionary[nums2[j]] += 1
            else:
                dictionary[nums2[j]] = 1
        
        min_key = float('inf')
        flag = 0

        for key in dictionary:
            if dictionary[key] >= 2:
                min_key = min(min_key, key)
                flag += 1
        
        if flag == 0:
            return -1
        else:
            return min_key