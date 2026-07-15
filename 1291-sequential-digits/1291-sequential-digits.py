class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        min_length = len(str(low))
        max_length = len(str(high))
        ans = []
        for length in range(min_length, max_length+1):
            adder = int('1'*length)
            start_num = int('123456789'[:length])
            print(f'adder:  {adder}')
            print(f'start_num:  {start_num}')
            for i in range(1, 10-length+1):
                if start_num % 10 != 0 and start_num <= high and start_num >= low:
                    ans.append(start_num)
                start_num += adder
        return ans