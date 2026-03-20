import numpy as np            #numpy 파일 다운이 안 되어 있다

a=np.array([4,5,0,1,2,3,6,7,8,9,10,11])
print(a)
print(type(a))
print(a.shape)
a.sort()
print(a)

b=np.array([-4.3,-2.3,12.9,8.99,10.1,-1.2])
b.sort()           # 오름차순 정렬
print(b)

c=np.array(['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
c.sort()            # 알파벳 순서로 정렬
print(c)