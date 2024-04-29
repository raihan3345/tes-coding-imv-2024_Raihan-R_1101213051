a = input("Masukkan kata pertama: ")
b = input("Masukkan kata kedua: ")
str1 = sorted(a.lower())
str2 = sorted(b.lower())

def isAnagram():
    if (str1 == str1) :
        return f"{a} dan {b} adalah anagram"
    else:
        return f"{a} dan {b} bukan anagram"

print(isAnagram())
