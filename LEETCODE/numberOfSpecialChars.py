def main():
    word = "abBCab"
    check_algorithm = MainNumofSpecialChar(word)
    return (check_algorithm.numberOfSpecialChars3())

class MainNumofSpecialChar:
    def __init__(self, word):
        self.word = word
    def numofSpecialChar(self):
        ans = 0
        check = {"a": 0, "b": 0, "c": 0}

        for i in range(len(self.word)):
            letter = self.word[i]
            if letter.isupper():
                letter = self.word[i].lower()
                if check[letter] == 1:
                    check[letter] += 1
                else:
                    check[letter] = 1
            else:
                check[letter] += 1
            if check[letter] == 2:
                ans += 1
        return ans
    def numofSpecialChar2(self):
        ans = 0
        check = {"a": 0, "b": 0, "c": 0}

        for i in range(len(self.word)):
            letter = self.word[i]
            if letter.isupper():
                letter = self.word[i].lower()
                if check[letter] == 0 or check[letter] == 1:
                    check[letter] += 2
            else:
                if check[letter] == 0 or check[letter] == 2:
                    check[letter] += 1
            if check[letter] == 3:
                ans += 1
                check[letter] += 1
                
        return ans
    def numberOfSpecialChars3(self) -> int:
        ans = 0
        check = {}

        for i in range(len(self.word)):
            letter = self.word[i]
            if letter.isupper():
                letter = self.word[i].lower()
                
                if letter not in check:
                    check[letter] = 0
                    
                if check[letter] == 0 or check[letter] == 1:
                    check[letter] += 2
            else:
                if letter not in check:
                    check[letter] = 0
                    
                if check[letter] == 0 or check[letter] == 2:
                    check[letter] += 1
                    
            if check[letter] == 3:
                ans += 1
                check[letter] += 1
                
        return ans


print(main())