class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def create_valid_parenthesis(left: int, right: int, s: str):
            if left == 0 and right == 0:
                result.append(s)
                return
            
            if left > 0:
                create_valid_parenthesis(left-1, right, s+'(')
            
            if right > left:
                create_valid_parenthesis(left, right-1, s+')')
        
        create_valid_parenthesis(n,n,'')
        return result

                
