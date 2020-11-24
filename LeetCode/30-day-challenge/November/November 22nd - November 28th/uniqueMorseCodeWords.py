class Solution:
    def uniqueMorseRepresentations(self, words):
        alphabets = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        frequency = {}
        for word in words:
            word_ = ""
            for alph in word:
                word_ += alphabets[ord(alph) - 97]
                
            frequency[word_] = frequency.get(word_, 0) + 1
        
        return len(frequency)
        

def main():
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

main()