#Create and Display an Array of 10 integers,iterate each index and compute the sum
import array as arr
a = arr.array('i', [1,2,3,4,5,6,7,8,9,10])

print("Entire Array: ")
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])

sum_of_array= sum(a)
print ("\n The sum of the array is: ", sum_of_array)
