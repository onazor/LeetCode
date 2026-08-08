import math

class Solution:
    def get_product(self, s_num, t):
            prod = 1
            for char in s_num:
                prod = math.gcd(prod * int(char), t)
            return prod

    def minimum_number(self, num, t):
            if self.get_product(num, t) == t:
                return num

            prefix_gcd = [1] * (len(num) + 1)
            for i in range(len(num)):
                prefix_gcd[i+1] = math.gcd(prefix_gcd[i] * int(num[i]), t)

            slot = 1
            final_idx = -1
            best_d = -1
            
            for idx in range(len(num)-1, -1, -1):
                current_product = prefix_gcd[idx]
                
                for d in range(int(num[idx]) + 1, 10):
                    target_needed = t // math.gcd(t, current_product * d)
                    temp_tgt = target_needed
                    req_slots = 0
                    for divisor in range(9, 1, -1):
                        while temp_tgt % divisor == 0:
                            req_slots += 1
                            temp_tgt //= divisor
                    
                    if temp_tgt == 1 and req_slots <= (slot - 1):
                        final_idx = idx
                        best_d = d
                        break
                
                if final_idx != -1:
                    break
                
                slot += 1
            
            if final_idx == -1:
                return ""
            
            final_string = num[:final_idx] + str(best_d)
            target = t // math.gcd(t, prefix_gcd[final_idx] * best_d)
            suffix_string = ''
            
            for _ in range(slot - 1):
                for num_slot in range(9, 0, -1):
                    if target % num_slot == 0:
                        suffix_string += str(num_slot)
                        target = target // num_slot
                        break

            return final_string + suffix_string[::-1]

    def smallestNumber(self, num: str, t: int) -> str:
        check_prime = t
        while True:
            if check_prime == 1:
                break
            if check_prime % 2 == 0:
                check_prime = check_prime // 2
            elif check_prime % 3 == 0:
                check_prime = check_prime // 3
            elif check_prime % 5 == 0:
                check_prime = check_prime // 5
            elif check_prime % 7 == 0:
                check_prime = check_prime // 7
            else:
                return "-1"

        zero_idx = num.find('0')
        if zero_idx != -1:
            num = num[:zero_idx] + '1' * (len(num) - zero_idx)
            
        new_num = self.minimum_number(num, t)

        while not new_num or self.get_product(new_num, t) != t:
            num = '1' * (len(num) + 1)
            new_num = self.minimum_number(num, t)

        return str(new_num)