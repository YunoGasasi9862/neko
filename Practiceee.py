class A:
     def __init__(self,m1,m2):
         self.m1=m1
         self.m2=m2



     def __add__(self, other):
         m1=self.m1 + other.m1
         m2=self. m2 + other.m2

         S3=A(m1,m2)
         return S3


     def __mul__(self, other):
         m1=self.m1 * other.m1
         m2=self.m2 * other.m2

         S3=A(m1,m2)
         return S3
     def __sub__(self, other):
         m1= self.m1 - other.m1
         m2= self.m2 - other.m2

         S3=A(m1,m2)
         return S3

     def __abs__(self):
        m1=self.m1
        m2=self.m2


        S3=A(m1,m2)
        return S3




S1= A(55,323)
S2=A(31245,232)
S3=S1-S2

print(S3.m1)
print(S3.m2)