def max_harvest(arr):
    max_harvest = 0
    n = len(arr)

    for i in range(n - 1):
        scenario1 = arr[i] + arr[i + 1]
        scenario2 = arr[i] + arr[i + 1] + arr[i + 2] if i + 2 < n else 0
        max_harvest += max(scenario1, scenario2)

    return max_harvest


arr = [5, 8, 6, 4, 9, 2, 7, 3]
result = max_harvest(arr)
print(result)