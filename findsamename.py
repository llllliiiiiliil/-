def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1 , n):
            print(f"{a[i]} - {a[j]}")
    return result

name = ["Tom","Jerry","Mike","Tom"]
print(find_same_name(name))