e1=int(input("公開鍵の指数を入力してください:"))
c1=int(input("その公開鍵で暗号化された文を入力してください:"))
e2=int(input("もう一つの公開鍵の指数を入力してください:"))
c2=int(input("その公開鍵で暗号化された文を入力してください:"))
n=int(input("公開鍵のモジュラスを入力してください:"))

def extended_gcd(a, b):
    if b == 0:
        return 1,0
    x1, y1 = extended_gcd(b, a % b)
    x=y1
    y=x1 -a//b*y1
    print("x="+str(x)+",y="+str(y)+",a="+str(a)+",b="+str(b))
    return x,y

def CommonModulesAttack(n, e1, e2, c1, c2):
    # n = 公開鍵のモジュラス
    # e1, e2 = 公開鍵の指数
    # c1, c2 = 暗号文
    a, b = extended_gcd(e1, e2)
    m = pow(c1, a, n)*pow(c2,b,n)

    return m%n

m = CommonModulesAttack(n, e1, e2, c1, c2)
print("復号された平文は"+ str(m))