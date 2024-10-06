def maxSubArraySum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Usage
arr = [3,-1,2,5,-6,3]
print(maxSubArraySum(arr))  # Output: 6
