#  pip install numpy
import numpy as np

a = np.array([1,2,3,4])
b=np.arange(4);
print(a);
print(b) ;
print((a+b),(a-b),(a*b))

print(np.zeros((1,2,3)));
print(np.ones(4));
print(np.ones((2,2)));
print(np.linspace(1,2,5)) #five values b/w 1 and 2


print("\n");
print("\n");
# indexing and slicing
arr = np.array([10,20,30,40,50]);
print(arr[0]);
print(arr[0:2]);
print(arr[1:4]);

print("\n")
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(matrix);
print(matrix[0][1])
print(matrix[1][1])
print(matrix[2][1])
print("")
print(matrix[0,1])
print(matrix[1,1])
print(matrix[2,1])
print("")
print(matrix[:,1]);
print("")
print(matrix[1,:]);
print("")

#getting input from the user
newArr=np.zeros(5);
print(newArr.size);
for i in range(0,newArr.size,1):
        newArr[i]=int(input("Enter number:"))
print(newArr)

#numpy array methods
print(np.mean(newArr));#average
print(np.median(newArr));#mid
print(np.sum(newArr));#sum
print(np.max(newArr));#maximum
print(np.min(newArr));#min
