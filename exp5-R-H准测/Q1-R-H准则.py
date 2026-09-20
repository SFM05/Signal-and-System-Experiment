import numpy as np


def RouthHurwitzPrinciple(coef: np.ndarray) -> tuple[np.ndarray, bool]:
    length = len(coef)
    rows = length
    cols = length//2 if length % 2 == 0 else length//2+1
    criterionMatrix = np.zeros((rows, cols))
    criterionMatrix[0, 0:cols] = coef[0:length:2]
    criterionMatrix[1,
                    0:(cols if length % 2 == 0 else cols-1)] = coef[1:length:2]

    for i in range(2, rows):
        for j in range(0, cols-1):
            det = np.linalg.det([[criterionMatrix[i-2, 0], criterionMatrix[i-2, j+1]],
                                 [criterionMatrix[i-1, 0], criterionMatrix[i-1, j+1]]])
            criterionMatrix[i, j] = -det/criterionMatrix[i-1, 0]

    negatives = np.sum(criterionMatrix[:, 0] < 0)
    if coef[0] > 0 and negatives > 0:
        stable = False
    elif coef[0] < 0 and negatives != length:
        stable = False
    else:
        stable = True

    return (criterionMatrix, stable)


coef = np.array([1, 1, 4, 1])
A, result = RouthHurwitzPrinciple(coef)
print(A)
print(result)
