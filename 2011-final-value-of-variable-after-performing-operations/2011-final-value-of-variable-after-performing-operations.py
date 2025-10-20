class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        start = 0
        for operation in operations:
            if "+" in operation:
                start += 1
            else:
                start -= 1
        return start

        