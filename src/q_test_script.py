import csv
import numpy as np

def make_q_table():
    q_table = {}
    with open('data/q_crit_vals.csv', newline='') as csvfile:
        confidence_values = []
        for row in csv.reader(csvfile, delimiter=','):
            if row[0] == 'N':
                for element in row:
                    confidence_values.append(element)
            else:
                q_vals_for_sample_size_N = {}
                for i in range(len(row)):
                    q_vals_for_sample_size_N[confidence_values[i]]= row[i]
                q_table[row[0]] = q_vals_for_sample_size_N
    return q_table

def find_q_crit(sample_size_n, confidence):
    q_table = make_q_table()
    return float(q_table[str(sample_size_n)]['%.2f' % confidence])

def remove_outlier(sorted_values, confidence, lower_q_exp, upper_q_exp):
    q_crit = find_q_crit(len(sorted_values), confidence)
    if lower_q_exp > q_crit and lower_q_exp > upper_q_exp:
        return sorted_values[1:]
    elif upper_q_exp > q_crit:
        return sorted_values[0:-1]
    return sorted_values

def q_exp_lt_8(sorted_values): 
    lower_q_exp = float(sorted_values[1]-sorted_values[0])/float(sorted_values[-1]-sorted_values[0])
    upper_q_exp = float(sorted_values[-1]-sorted_values[-2])/float(sorted_values[-1]-sorted_values[0])
    return lower_q_exp, upper_q_exp

def q_exp_lt_11(sorted_values):
    lower_q_exp = float(sorted_values[1]-sorted_values[0])/float(sorted_values[-2]-sorted_values[0])
    upper_q_exp = float(sorted_values[-1]-sorted_values[-2])/float(sorted_values[-1]-sorted_values[1])
    return lower_q_exp, upper_q_exp

def q_exp_lt_14(sorted_values):
    lower_q_exp = float(sorted_values[2]-sorted_values[0])/float(sorted_values[-2]-sorted_values[0])
    upper_q_exp = float(sorted_values[-1]-sorted_values[-3])/float(sorted_values[-1]-sorted_values[1])
    return lower_q_exp, upper_q_exp

def q_exp_lt_31(sorted_values):
    lower_q_exp = float(sorted_values[2]-sorted_values[0])/float(sorted_values[-3]-sorted_values[0])
    upper_q_exp = float(sorted_values[-1]-sorted_values[-3])/float(sorted_values[-1]-sorted_values[2])
    return lower_q_exp, upper_q_exp

def remove_outlier_via_q_test(input_data, confidence = 0.95):
    sorted_input = np.sort(input_data)
    # If for some reason it's uniform (would cause division by zero, return as is
    if sorted_input[0] == sorted_input[-1]: 
        return sorted_input
    sample_size_n = len(sorted_input)
    lower_q, upper_q = 0, 0
    if sample_size_n < 3 or sample_size_n > 30:
        print('Sample size must be between 3 and 30 for the q-test to be usable')
    elif sample_size_n < 8:
        lower_q, upper_q = q_exp_lt_8(sorted_input)
    elif sample_size_n < 11:
        lower_q, upper_q = q_exp_lt_11(sorted_input)
    elif sample_size_n < 14:
        lower_q, upper_q = q_exp_lt_14(sorted_input)
    else:
        lower_q, upper_q = q_exp_lt_31(sorted_input)
    return remove_outlier(sorted_input, confidence, lower_q, upper_q )

if __name__ == '__main__':
    print("**********************************************************************")
    print( remove_outlier_via_q_test([1,1,1,1,1]))

    print("**********************************************************************")