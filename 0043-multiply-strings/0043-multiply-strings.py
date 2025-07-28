class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1_length = len(num1)
        num2_length = len(num2)

        list_ints1 = []
        for idx in range(num1_length-1, -1, -1):
            tenth_pow = 10**idx
            list_ints1.append(tenth_pow*int(num1[num1_length-idx-1]))

        list_ints2 = []
        for idx in range(num2_length-1, -1, -1):
            tenth_pow = 10**idx
            list_ints2.append(tenth_pow*int(num2[num2_length-idx-1]))
        
        product = 0
        for i in range(len(list_ints1)):
            for j in range(len(list_ints2)):
                product += list_ints1[i]*list_ints2[j]

        return str(product)
                
