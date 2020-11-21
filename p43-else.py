
for item in range(3):
    password = input(" パスワードを入力してください")
    if password == "8888":
        print("パスワードが正しいです")
        break
    else:
        print(" パスワードが正しくないです")
else:
    print("入力不可-入力ミスは3回まで")


print("..........................")

a = 0
while a <3:
    password = input("パスワードを入力してください")
    if password == "8888":
        print("パスワードが正しいです")
        break
    else:
        print("パスワードが正しくないです")
        a += 1
else:
    print("入力不可-入力ミスは3回まで")
