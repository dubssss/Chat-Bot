

def getcredentials():
    with open('/root/credentials.txt', 'r') as f:
        x=f.read().splitlines()
    return x

if __name__=="__main__":
    getcredentials()
