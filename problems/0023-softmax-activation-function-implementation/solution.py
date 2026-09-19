import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores = np.asarray(scores, dtype = float)
    temp = np.exp(scores - np.max(scores))

    return (temp / (np.sum(temp))).tolist()



