c = input("シーサー暗号文を入力してください:")
n=int(input("シフト数を入力してください:"))

words=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Words=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

chars=list(c)
for i in range(len(c)):
    for j in range(len(words)):
        if chars[i] == words[j]:
            if j + n < len(words):
                chars[i]=words[j+n]
            else:
                chars[i]=words[(j+n)%len(words)]
            break
        elif chars[i] == Words[j]:
            if j + n < len(Words):
                chars[i]=Words[j+n]
            else:
                chars[i]=Words[(j+n)%len(Words)]
            break
        elif j < len(nums) and chars[i] == nums[j]:
            if j + n < len(nums):
                chars[i]=nums[j+n]
            else:
                chars[i]=nums[(j+n)%len(nums)]
            break
print("シーサー暗号文は" + ''.join(chars))