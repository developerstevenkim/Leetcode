class Solution:
    @staticmethod
    def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
        def go(word):
            ans = 0
            for c in word:
                ans *= 10
                ans += ord(c) - ord('a')
            return ans
        return go(firstWord) + go(secondWord) == go(targetWord)

def main():
    solution = Solution
    print(solution.isSumEqual('aaa', 'a', 'aab'))


if __name__ == '__main__':
    main()
