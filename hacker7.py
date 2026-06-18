def miniMaxSum(arr):
    my_list = []
    total_sum = sum(arr) # Calculated once outside the loop for speed
    
    for i in range(len(arr)):
        k = total_sum - arr[i]
        my_list.append(k)
        
    s = min(my_list)
    l = max(my_list)
    
    # FIX 1: Print the result separated by a space instead of returning
    print(s, l) 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
