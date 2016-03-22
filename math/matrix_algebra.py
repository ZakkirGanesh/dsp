# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:39:20 2016

@author: azg
"""
import numpy as np

# Program to multiply two matrices using nested loops

# A is a 2x3 matrix
A = np.array([[1,2,3],[2,7,4]])
# B is a 2x2 matrix
B = np.array([[1,-1],[0,1]])
# C is a 3x2 matrix
C = np.array([[5,-1],[9,1],[6,0]])
# D is a 2X3 matrix
D = np.array([[3,-2,-1],[1,2,3]])
# u is a 1x4 vector
u = np.array([6,2,-3,5],)
# v is a 1x4 vector
v = np.array([3,5,-1,4],)
# w is a 4x1 vector
w = np.array([[1],[8],[0],[5]])
# alpha is a scalar
alpha = 6
# 1.1 dimensions of A
print(A.shape)
# 1.2 dimensions of B
print(B.shape)
# 1.3 dimensions of C
print(C.shape)
# 1.4 dimensions of D
print(D.shape)
# 1.5 dimensions of u
print(u.shape)
# 1.6 dimensions of v
print(v.shape)
# 1.7 dimensions of w
print(w.shape)
# 2.1 u + v
u_plus_v = [x+y for x,y in zip(u,v)]
print(u_plus_v)
# 2.2 u - v
u_minus_v = [x-y for x,y in zip(u,v)]
print(u_minus_v)
# 2.3 alpha * u
alpha_times_u = [x*alpha for x in u]
print(alpha_times_u)
# 2.4 dot product of u and v
u_v_dot_product = sum([x*y for x,y in zip(u,v)])
print(u_v_dot_product)
# 2.5 u normed
u_normed = np.sqrt(sum([x**2 for x in u]))
print(u_normed)
# 3.1 A + C (should return error due to mismatched shapes)
def matrix_add(x,y):
    if(x.shape == y.shape):
        return x + y
    else:
        return "Undefined."

A_plus_C = matrix_add(A,C)
print(A_plus_C)
# 3.2 A - C-transposed
def matrix_subtract(x,y):
    if(x.shape == y.shape):
        return x - y
    else:
        return "Undefined."

A_minus_C_trans = matrix_subtract(A,np.transpose(C))
print(A_minus_C_trans)
# 3.3 C-transposed + 3D
C_trans_plus_3D = matrix_add(np.transpose(C),3*D)
print(C_trans_plus_3D)
# 3.4 B times A
def matrix_multiply(x,y):
    if(x.shape[1] == y.shape[0]):
        return np.dot(x,y)
    else:
        return "Undefined."
B_times_A = matrix_multiply(B,A)
print(B_times_A)
# 3.5 B times A-transposed
B_times_A_trans = matrix_multiply(B,np.transpose(A))
print(B_times_A_trans)
