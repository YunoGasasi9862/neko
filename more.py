class det():
    def __init__(self,m1):
        self.m1=m1


    def __abs__(self):
        m1= abs(self.m1)


        answer=det(m1)
        return answer

s1=det(--66)


answer=abs(s1)
print(answer.m1)



