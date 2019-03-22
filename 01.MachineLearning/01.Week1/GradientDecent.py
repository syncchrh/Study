import numpy as np

x = np.matrix('1; 2; 3; 4')
y = np.matrix('4; 6; 8; 10')


(m, n) = x.shape

thetaZero = np.random.randn()
thetaOne = np.random.randn()

#hypothesis = thetaZero + thetaOne*x

#Variable initialize

costSum = 0
costResult = 0

thetaZeroResult = 0
thetaOneResult = 0
learning_rate = 0.01


for epoch in range(5000):
    #CostFunction
    for i in range(m):
        costSum = thetaZero + thetaOne * x[i] - y[i]
        costSum = costSum * costSum
        costResult = costResult + costSum
    costResult = costResult / (2*m)
    print("Epoch: ", epoch, "Cost : ", costResult, "thetaZero : ", thetaZero, "thetaOne : ", thetaOne)

    if costResult < 0.0001:
        break

    #FindTheta
    for i in range(m):
        # thetazero
        sumThetaZero = thetaZero + thetaOne * x[i] - y[i]
        thetaZeroResult = thetaZeroResult + sumThetaZero
        # thetaone
        sumThetaOne = (thetaZero + thetaOne * x[i] - y[i]) * x[i]
        thetaOneResult = thetaOneResult + sumThetaOne

    thetaZeroResult = thetaZeroResult / m
    thetaZeroResult = learning_rate * thetaZeroResult
    thetaOneResult = thetaOneResult / m
    thetaOneResult = learning_rate * thetaOneResult

    thetaZero = thetaZero - thetaZeroResult
    thetaOne = thetaOne - thetaOneResult

#Test
input = 8
tempResult = thetaZero + thetaOne*input
print("if input = 8, output = ", tempResult)






