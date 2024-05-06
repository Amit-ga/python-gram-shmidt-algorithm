import numpy as np
import math
import sys

# Returns true if mat[N][N] is symmetric, else false
def is_symmetric(mat, n):
    for i in range(n):
        for j in range(n):
            if mat[i][j] != mat[j][i]:
                return False
    return True


def is_positive_definite(mat):
    lambdas, v = np.linalg.eig((np.array(mat)).T)
    if min(lambdas) <= 0:
        return False
    if not(is_symmetric(mat, 3)):
        return False
    return True


def is_zero_vec(vec):
    for elem in vec:
        if abs(elem) <= sys.float_info.epsilon:
            elem = 0
    return np.array_equal(vec, np.zeros(len(vec)))


def is_base(vec_list, dim):
    if len(vec_list) != dim:
        return False
    if is_zero_vec(vec_list[dim-1]):
        return False
    return True


def clear_zeroes(lst):
    cleared = []
    for obj in lst:
        if not(is_zero_vec(obj)):
            cleared.append(obj)
    return cleared


def inner_product(vec1, vec2, mat):
    vec1T = np.transpose(vec1)
    scalar = np.dot(vec1T, (np.dot(mat, vec2)))
    return scalar

def gramsh_calc(vec_list, inner_product_matrix):
    local_vec_list = clear_zeroes(vec_list)
    gs_list = []
    for i in range(0, len(local_vec_list)):
        temp_scalar = math.sqrt(inner_product(local_vec_list[i], local_vec_list[i], inner_product_matrix))
        if abs(temp_scalar) < sys.float_info.epsilon*pow(10, 4):
            continue
        gs_list.append((np.true_divide(local_vec_list[i], temp_scalar)))
        for j in range(i+1, len(local_vec_list)):
            temp_scalar = inner_product(local_vec_list[j], gs_list[i], inner_product_matrix)
            temp_vec = np.dot(gs_list[i], temp_scalar)
            local_vec_list[j] = np.subtract(local_vec_list[j], temp_vec)
    clear_zeroes(gs_list)
    return gs_list


def print_base(base: list):
    for mat in base:
        print(np.matrix(mat))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # A basic code for matrix input from user
    # Initialize matrix
    first_pass = True
    while first_pass or not(is_positive_definite(matrix)):
        matrix = []
        first_pass = False
        if not first_pass:
            print("Input matrix must be positive definite")
        print("Enter the entries rowwise:")
        # For user input
        for i in range(3):  # A for loop for row entries
            temp = []
            for j in range(3):  # A for loop for column entries
                temp.append(int(input()))
            matrix.append(temp)

    dim = 3
    first_pass = True
    span_size = 4
    while first_pass or not(span_size <= 3):
        if first_pass:
            span_size = int(input("Please enter the number of vectors you would like to GS: "))
            first_pass = False
            continue
        span_size = int(input("Number of vector must be less than 4 \n "))

    vec_list = []
    # creating an empty list
    # iterating till the range
    for i in range(0, span_size):
        temp_lst = []
        for j in range(0, dim):
            element = int(input())
            temp_lst.append(element)
        vec_list.append(temp_lst)
    gs = gramsh_calc(vec_list, matrix)
    print("Your GS group is:")
    print_base(gs)
    if is_base(gs, dim):
        print("and it is an orthonormal base!")
    else:
        print("and it is not an orthonormal base!")
