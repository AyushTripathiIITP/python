if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    m1 = max(arr)
    m2 = -999
    for i in range(0 , n):
        if(arr[i] != m1 and arr[i] > m2):
            m2 = arr[i]
print(m2)