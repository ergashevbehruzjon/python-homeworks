class Vector():
    def __init__(self,*nums):
        self.components=tuple(round(i,3) for i in nums)
    def __str__(self):
        return f"Vector{self.components}"
    def __add__(self,other):
        if len(self.components)!=len(other.components):
            raise ValueError("Cannot add different dimensional vectors")
        return Vector(*[i+j for i,j in zip(self.components,other.components)])
    def __sub__(self,other):
        if len(self.components)!=len(other.components):
            raise ValueError("Cannot subtract different dimensional vectors")
        return Vector(*[i-j for i,j in zip(self.components,other.components)])
    def dot(self,other):
        if len(self.components)!=len(other.components):
            raise ValueError("Cannot find dot product of different dimensional vectors")
        return sum(i*j for i,j in zip(self.components,other.components))
    def __mul__(self,other):
        if type(other)==int:
            return Vector(*[i*other for i in self.components])
        elif type(other)==Vector:
            return self.dot(other)
        else:
            raise TypeError(f"Cannot multiply Vecotr with type '{type(other)}'")
    def __rmul__(self,other):
        return self.__mul__(other)
    def magnitude(self):
        return sum(i**2 for i in self.components)**.5
    def normalize(self):
        magn=self.magnitude()
        if magn==0:
            raise ValueError("Cannot normalize i zero vector")
        return Vector(*[i/magn for i in self.components])
    
# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)