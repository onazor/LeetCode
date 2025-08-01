class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list_result = []
        for row in range(1, numRows+1):
            list_temp = [0]*row
            if row == 1:
                list_result.append([1])
            elif row == 2:
                list_result.append([1,1])
            else:
                list_temp[0] = 1
                list_temp[-1] = 1
                for idx in range(1, row-1):
                    prev_list = list_result[-1]
                    list_temp[idx] = prev_list[idx-1]+prev_list[idx]
                list_result.append(list_temp)
        return list_result
            
