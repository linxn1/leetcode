from typing import List


class Solution:
    def __init__(self):
        self.dict_keys = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        def backtrack(start_index, path):
            if len(path) == len(digits):
                result.append(''.join(path[:]))
                return
            for i in range(start_index, len(digits)):
                for j in self.dict_keys[int(digits[i])]:
                    path.append(j)
                    backtrack(start_index=i + 1, path=path)
                    path.pop()

        result = []
        backtrack(start_index=0, path=[])

        return result


print(Solution().letterCombinations("23"))
