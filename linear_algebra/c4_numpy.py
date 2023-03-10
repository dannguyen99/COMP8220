# # create array
# from numpy import array, empty
# l = [1.0, 2.0, 3.0]
# a = array(l)
# # display array
# print(a)
# # display array shape
# print(a.shape)
# # display array data type
# print(a.dtype)

# # create empty array
# a = empty([3,3])
# print(a)

#create array with vstack
# from numpy import array
# from numpy import vstack
# # create first array
# a1 = array([1,2,3])
# print(a1)
# # create second array
# a2 = array([4,5,6])
# print(a2)
# # vertical stack
# a3 = vstack((a1, a2))
# print(a3)
# print(a3.shape)

# index two-dimesional array
from numpy import array
# define array
data = array([
    [11,22],
    [33,44],
    [55,66]])

print(data[0,0])