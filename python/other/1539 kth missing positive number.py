arr = [2,3,4,7,11]
k = 5

gap = 0

for i in range(len(arr)):
    if i == 0:
        if arr[i] != 1:
            gap = arr[i] - 1

            if k > gap:
                k-=gap

            elif k <= gap:
                print(k)
                break
    else: 
        gap = arr[i] - arr[i-1] - 1
        if k > gap:
            k-=gap
        elif k <= gap:
            print(arr[i-1] + k)
            break
