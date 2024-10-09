from random import random
from typing import List


class Master:
    def __init__(self, secret):
        self.secret = secret

    def guess(self, word):
        matches = 0
        for i in range(6):
            if word[i] == self.secret[i]:
                matches += 1
        return matches


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        if not words:
            return

        guess = words[len(words) // 2]
        filtered_words = words
        count = 0
        while filtered_words:
            filtered_words.remove(guess)
            count += 1
            score = master.guess(guess)
            if score == 6:
                break

            filtered_words = filter_words(filtered_words, guess, score)
            guess = random.choice(filtered_words)


def filter_words(words, guess, score):
    new_words = []
    for word in words:
        matches = 0
        for i in range(6):
            if word[i] == guess[i]:
                matches += 1
        if score == 0 and matches == 0:
            new_words.append(word)
        if score != 0 and matches == score:
            new_words.append(word)
    return new_words


def main():
    words = ["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc",
             "bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr",
             "uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad",
             "uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn",
             "kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa",
             "kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty",
             "dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg",
             "vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh",
             "reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus",
             "pydgmq"]

    master = Master("ccoyyo")
    print(findSecretWord(words, master))

main()