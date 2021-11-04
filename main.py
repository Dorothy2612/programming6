import sys
def latin(c):
    vow = ["a", "e","i","o","u"]
    if c[0] in vow:
        return c+"yay"
    else:
        a = ""
        s = ""
        counter = 0
        while (c[counter] not in vow):
            s+=c[counter]
            counter+=1
        return c[counter:]+s+'ay'
if __name__ == '__main__':
     user = input("Enter the sentence: ")
     lis = user.split(" ")
     print(lis)
     result=""
     for b in lis:
         result+=latin(b)+' '
     print(result)




