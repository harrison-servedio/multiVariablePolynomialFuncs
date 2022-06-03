# import numpy as np
# x = np.array([2.0, 4.0, 5.0,-1])
# y = np.array([1.0, -3.0])
# a, b = np.polydiv(x, y)
# print(np.polydiv(a, b))

# # (array([0.01923077, 0.09615385, 0.33653846]), array([0.]))


# def recursive_test(integer):
#     l = []
#     if integer == 2:
#         l.append('done')
#     else:
#         l.append(integer)
#         l.extend(recursive_test(integer - 1))
#     return l

# print(recursive_test(10))



m = 5
n = m

n += 1
print(m)