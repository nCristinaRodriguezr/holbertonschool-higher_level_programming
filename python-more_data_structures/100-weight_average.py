#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result_mul = 0
    sum_weight = 0
    for tupi in my_list:
        result_mul = tupi[0] * tupi[1] + result_mul
        sum_weight = sum_weight + tupi[1]
    return (result_mul / sum_weight)
    
    
    