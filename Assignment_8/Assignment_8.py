import numpy as np
Q=np.array([[-0.7071,0.7071],[0.7071,-0.7071]])
R=np.array([[0.7071,-0.7071],[0,0]])
result=Q@R
print(result)