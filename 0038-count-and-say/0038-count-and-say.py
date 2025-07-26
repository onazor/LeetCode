class Solution:
    def countAndSay(self, n: int) -> str:
        def mapper(num: str):
            length = len(num)
            prev = num[0]
            count = 1
            result = []

            int_num = int(num)
            for i in range(1, len(num)):
                if num[i] == prev:
                    count += 1
                    prev = num[i]
                else:
                    result.append([prev, count])
                    count = 1
                    prev = num[i]
            
            result.append([int(prev), count])
            return result
        
        def creater(dbl_list: List[List[int]]):
            result = ""
            for lst in dbl_list:
                temp = str(lst[1]) + str(lst[0])
                result += temp
            return result

        if n == 1:
            return '1'
        
        base = '1'
        for _ in range(2, n+1):
            freq = mapper(base)
            result = creater(freq)
            base = result

        return result
            
                    

                

