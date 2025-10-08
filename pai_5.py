import numpy as np
apple = np.array([1,2,3,4,5,8])
print(type(apple))

#rank : number of dimensions
#shape : number of elements in each dimension

apple2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print([apple2])

print("lent of 1d array", len(apple))
print("lent of 2d array", len(apple2))

apple3 = np.array([[1,2,3],[4,5,6]])
print(apple3)

alpha = np.zeros(7)
print(alpha)

beta  = np.ones(50)
print(beta)

gamma = np.empty(5)
print(gamma)

cheeta = np.arange(10)
print(cheeta)

theeta = np.arange(5,10)
print(theeta)

cutu = np.arange(2,20,2)
print(cutu)

motu = np.linspace(0,5,9)
print(motu)

#generate random data in numpy array
fruitu = np.random.rand(2,3) #2 rows , 3 columns
print("tidays work\n\n\n",fruitu)
#randa

print("\n",fruitu*10)
print("\n",fruitu*fruitu)
print(np.add(fruitu,fruitu))
print(fruitu+6)

#define a single angle in degrees
angle_degrees = 45 # 45 degrees

# calculate sin, cos,and tan of the angle
sin_value = np.sin(angle_degrees)
cos_value = np.cos(angle_degrees)  
tan_value = np.tan(angle_degrees)  

#print the results
print("angle degrees",angle_degrees)
print("sin:",sin_value)
print("cos:",cos_value)
print("tan:",tan_value)

#create a ID array (vector)
array_id = np.array([1,2,3,4,5])
print("ID Array:\n",array_id)
print("Shape: ", array_id.shape)
print("Data type :", array_id.dtype)

print()

#create a 2D array (matrix)
array_2d = np.array([[1,2,3],
                    [4,5,6]])
print("2D array:\n", array_2d)
print("shape:",array_2d.shape)
print("Data type :", array_2d.dtype)

print()

#create a 3D array (tensor)
array_3d = np.array([[[1,2],
                    [3,4]],
                    [[5,6],
                    [7,8]]])
print("2D array:\n", array_3d)
print("shape:",array_3d.shape)
print("Data type :", array_3d.dtype)
print()

#create an array with a specific data type (float)
array_float = np.array([1.0,2.0,3.0],dtype = np.float32)
print("print array with specific dtype (float32):\n",array_float)
print("shape:",array_float.shape)
print("Data type :", array_float.dtype)
print()

empty_array = np.empty((3,4))
#creates an uninitialized array with shape (3,4)
print("empty array:\n",empty_array)
print("shape:",empty_array.shape)
print("Data type :", empty_array.dtype)
print()

print(array_3d.size)

#the ndim attribute is used to determine the dimensions of the array
print("use of:",array_3d.ndim)
print(array_3d.shape)
print(array_3d.nbytes)

simple_array = np.array([[1,2,3,4,5],
                        [6,7,8,9,10]])
print(simple_array[1,2])

print(np.identity(3))

amatrix = np.array([[1,2],[3,4]])

print(np.linalg.det(amatrix))
print(np.trace(amatrix))
print(np.linalg.eigvals(amatrix))
print(np.linalg.inv(amatrix))

my_matrix = np.array([[10,20,30],[40,50,60]])

#sum along axis 0 column wise

sum_axis_0 = np.sum(my_matrix,axis = 0)
print("sum of axis 0 (columns): ",sum_axis_0 )

#sum along axis 1 row wise

sum_axis_1 = np.sum(my_matrix,axis = 1)
print("sum of axis 1 (rows): ",sum_axis_1 )

# understanding 