import math

x = [1, 2, 3, 4]
y = [1, 2, 3 ,4]


def mean(arr):
    return sum(arr)/len(arr)

meanx = mean(x)
meany = mean(y)

# print(meanx, meany)

def covariance(xarr, yarr):
    return sum((xarr[i] - mean(xarr)) * (yarr[i] - mean(yarr)) for i in range(len(xarr))) 

def sigma(xyarr):
    return  math.sqrt(sum((xyarr[i] - mean(xyarr)) ** 2 for i in range (len(xyarr))))


def correlation (xarr, yarr):
    return covariance(xarr, yarr) / (sigma(xarr) * sigma(yarr))

print(correlation(x, y))