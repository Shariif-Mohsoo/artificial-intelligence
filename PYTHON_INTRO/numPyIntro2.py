import numpy as np;

print(np.arange(25));
print(np.arange(25).reshape(5,5));
# print(np.arange(25).reshape(2,3,5));

print(np.arange(24).reshape(2,3,4));
print(np.arange(30).reshape(3,2,5));

arr=np.zeros((3,3));
print(arr);

print(arr.shape)
rows, cols = arr.shape  # Get rows and columns automatically

print("Array:\n", arr)
print(f"\nRows: {rows}, Columns: {cols}\n")

for i in range(rows):
    for j in range(cols):
        val = int(input("Enter value: "))
        arr[i][j]=val
        print(f"Value at position [{i},{j}] = {arr[i][j]}")


