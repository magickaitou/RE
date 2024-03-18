## Function create password from username
## Username: (ascii >= 'A')
## https://mega.nz/#!KbAWzK7D!LOnvJeYpXpxkMIH_jLGzx7VKVTQg1LifsFQMnOj_WeM

username = input()
sum_username = 0
for char in username:

    if(ord(char)<ord('A')):
        print("Invalid username")
        exit
    elif(ord(char)>=ord('Z')):
        sum_username += ord(char) - 32
    else:
        sum_username += ord(char)

username1= sum_username ^ 0x5678
print(hex(username1))

password = username1 ^ 0x1234
print(password)
