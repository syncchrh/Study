#if n is very large --> Slow because need to compute inverse(x_transpose*x)
#--> Use Gradient descent
import numpy as np

x = np.matrix('1, 1; 1, 2; 1, 3; 1, 4')
y = np.matrix('4; 6; 8; 10')

theta = np.linalg.inv(np.matrix.transpose(x)*x)*np.matrix.transpose(x)*y
print(theta)