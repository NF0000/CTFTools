strings = input("Unicodeに変換したい16進数を入力してください:")
split = input("区切り文字を入力してください:")

def anotherWord(a):
    if a == "Y":
        return int(input("何文字文切り取る必要がありますか？:"))
        
    elif a != "n" and a != "Y":
        anotherWord(input("文字コードの先頭に他の文字が存在しますか？:[Y/n]"))
    else:
        return 0

rm = anotherWord(input("文字コードの先頭に他の文字が存在しますか？:[Y/n]"))

s = strings.split(split)
print(s)

result = "以下が変換された文字です:"

for i in range(len(s)):
    result += (chr(int(s[i][rm:],16)))
print(result)