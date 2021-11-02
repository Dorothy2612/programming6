import sys
def bigletter():
    for item in (sys.argv):
        print(item.capitalize())
def n():
    for item in (sys.argv):
        print(item.count("is"))



if __name__ == '__main__':
    print(f"Arguments count: {len(sys.argv)}")
    for item in (sys.argv):
        print(item)
    bigletter()
    n()



