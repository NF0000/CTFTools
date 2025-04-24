# XOR復号.py
print("XOR復号を行います")
print('復号したい16進数(ex.0x7aの時は7a)を入力してください(入力が終了したらendを入力してください)')

nums = []
while True:
    num = "0x"+input("Enter a number(ex.7a): ")
    if num == "0xend":
        break
    nums.append(int(num,16))

print("復号したいXORの値を入力してください")
dec =int("0x"+input("Enter a XOR(ex.1b): "),16)

xor =[]
for i in range(len(nums)):
    xor.append(nums[i] ^ dec)
print("復号結果")
print(xor)
chrs=[]
for i in range(len(xor)):
    chrs.append(chr(xor[i]))
print("復号結果を文字列に変換")
print(chrs)
