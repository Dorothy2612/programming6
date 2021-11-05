import sys
def word2(a):
    m=a.replace(" ", "\n")
    print(m)
def word1(a):
    s=a.split(' ')
    for item in s:
        print(item)
if __name__ == '__main__':
    user = input("Enter the sentence: ")
    word1(user)
    word2(user)

