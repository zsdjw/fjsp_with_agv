import numpy as np

x = [[1,2,3],
    [4,5,6]
]
y = []
# x = np.array(x)
# y = []
# for i in range(x.shape[0]):
#     for z in range(x.shape[1]):
#         y.append(i)

for i in range(len(x)):
    for z in range(len(x[0])):
        y.append(i+1)
print(y)