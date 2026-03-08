class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        def generate_length_n(current_string):
            if len(current_string) == len(nums[0]):
                result.append(current_string)
                return 
            
            generate_length_n(current_string + '0')
            generate_length_n(current_string + '1')

        generate_length_n('')
        for binary in result:
            if binary not in nums:
                return binary 
        return None
