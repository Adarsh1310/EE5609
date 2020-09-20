import numpy as np
Q=np.array([[-0.7071,0],[0.7071,0]])
R=np.array([[0.7071,-0.7071],[0,0.707]])
result=Q@R
print(result)
