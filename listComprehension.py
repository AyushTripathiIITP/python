if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print ([[a,b,c] for a in (0 , x+1) for b in (0 , y+1) for c in (0, z+1)
    if(a+b+c != n)])
