import numpy as np
import sys


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


def gramsh_calc(vec_list):
    local_vec_list = clear_zeroes(vec_list)
    gs_list = []
    for i in range(0, len(local_vec_list)):
        temp_scalar = np.linalg.norm(local_vec_list[i])
        # numeric error correction
        if abs(temp_scalar) < sys.float_info.epsilon*pow(10, 4):
            continue
        gs_list.append((np.true_divide(local_vec_list[i], temp_scalar)))
        for j in range(i+1, len(local_vec_list)):
            temp_scalar = np.inner(local_vec_list[j], gs_list[i])
            temp_vec = np.dot(gs_list[i], temp_scalar)
            local_vec_list[j] = np.subtract(local_vec_list[j], temp_vec)
    clear_zeroes(gs_list)
    return gs_list


def print_base(base: list):
    for mat in base:
        print(np.matrix(mat))


def test1():
    matrix = [[1, 2, 2, 0], [0, -1, -1, 0], [0, 0, 0, 3], [2, 1, 1, 3]]
    return matrix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_pass = True
    dim = 0
    while first_pass or dim > 5:
        if first_pass:
            dim = int(input("Please enter space dimension: "))
            first_pass = False
            continue
        dim = int(input("Space dimension must be less than 6 \n"))

    first_pass = True
    span_size = 0
    while first_pass or span_size > 5:
        if first_pass:
            span_size = int(input("Please enter the number of vectors you would like to GS: "))
            first_pass = False
            continue
        span_size = int(input("Number of vector must be less than 6 \n"))

    vec_list = []
    # creating an empty list
    # iterating till the range
    for i in range(0, span_size):
        temp_lst = []
        for j in range(0, dim):
            element = int(input())
            temp_lst.append(element)
        vec_list.append(temp_lst)
    gs = gramsh_calc(vec_list)
    print("Your GS group is:")
    print_base(gs)
    if is_base(gs, dim):
        print("and it is an orthonormal base!")
    else:
        print("and it is not an orthonormal base!")
