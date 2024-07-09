class Solution:
    # Solution runs in O(n+m) time, where n, m is the length of ransomNote and magazine
    # and O(1) space.
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        note_letters_dict = create_letters_dict(ransomNote)
        mag_letters_dict = create_letters_dict(magazine)
        for letter in note_letters_dict:
            if letter not in mag_letters_dict:
                return False
            elif note_letters_dict[letter] > mag_letters_dict[letter]:
                return False
        return True


def create_letters_dict(word):
    letters_dict = {}
    for letter in word:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    return letters_dict
