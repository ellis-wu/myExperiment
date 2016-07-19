# -*- coding: utf-8 -*-
import csv
from datetime import datetime


def read_csv_file_to_list(filename):
    csv_list = []
    f = open(filename, 'r')
    for row in csv.reader(f):
        csv_list.append(row)
    f.close()
    return csv_list


def read_csv_file_to_dict(filename):
    csv_dict = {}
    f = open(filename, 'r')
    for row in csv.DictReader(f):
        for key, value in row.iteritems():
            csv_dict.setdefault(key, []).append(value)
    f.close()
    return csv_dict


def get_csv_max_and_min_key(filename):
    max_key = str(0)
    min_key = str(0)
    for key in read_csv_file_to_dict(filename):
        if float(key) > float(max_key):
            max_key = key
        elif float(key) < float(min_key):
            min_key = key
    return [min_key, max_key]


def get_up_and_low_value(filename, input_value):
    up_value = get_csv_max_and_min_key(filename)[1]
    low_value = get_csv_max_and_min_key(filename)[0]
    index = 0
    membership = read_csv_file_to_dict(filename)
    for key in membership:
        if float(input_value) <= float(key):
            if index == 0:
                up_value = key
            else:
                if float(key) < float(up_value):
                    up_value = key
            index += 1
        if float(input_value) >= float(key):
            if index == 0:
                low_value = key
            else:
                if float(key) > float(low_value):
                    low_value = key
            index += 1
    return [low_value, membership[low_value], up_value, membership[up_value]]


def get_membership(filename, input_value):
    up_and_low = get_up_and_low_value(filename, input_value)
    low_key = up_and_low[0]
    low_value = up_and_low[1]
    up_key = up_and_low[2]
    up_value = up_and_low[3]
    result = []
    for count in range(len(low_value)):
        if float(low_value[count]) - float(up_value[count]) < 0:
            m = (float(low_key) - float(up_key)) / (float(low_value[count]) - float(up_value[count]))
            membership_value = (float(input_value) - float(low_key)) / m + float(low_value[count])
        elif float(low_value[count]) - float(up_value[count]) > 0:
            m = (float(low_key) - float(up_key)) / (float(low_value[count]) - float(up_value[count]))
            membership_value = (float(input_value) - float(up_key)) / m + float(up_value[count])
        elif float(low_key) == float(up_key):
            membership_value = low_value[count]
        elif float(low_value[count]) == 1.0 and float(up_value[count]) == 1.0:
            membership_value = 1.0
        else:
            membership_value = 0.0
        if float(membership_value) > 0:
            result.append([count, membership_value])
    return result


def fuzzy_inference(ele1, ele2, rule_base):
    outputs = dict()
    for cpu_values in ele1:
        for memory_values in ele2:
            for rule in rule_base:
                if float(cpu_values[0]) == float(rule[0]) and float(memory_values[0]) == float(rule[1]):
                    # print rule[2], min(float(cpu_values[1]), float(memory_values[1]))
                    if rule[2] not in outputs:
                        outputs[rule[2]] = []
                    outputs[rule[2]].append(min(float(cpu_values[1]), float(memory_values[1])))
    result = {k: max(v) for k, v in outputs.iteritems()}
    return result


def fuzzy_defuzzification(inference):
    fuzzy_result_csv = read_csv_file_to_list('result-1.csv')
    tmp_dict = dict()
    for key, values in inference.iteritems():
        if key not in tmp_dict:
            tmp_dict[key] = []
        for index, value in enumerate(fuzzy_result_csv[int(key) + 1]):
            if float(value) != 0:
                if index - 1 >= 0 and index + 1 <= fuzzy_result_csv[0].index(max(fuzzy_result_csv[0])):
                    tmp_dict[key].append(fuzzy_result_csv[0][index - 1])
                    tmp_dict[key].append(fuzzy_result_csv[0][index])
                    tmp_dict[key].append(fuzzy_result_csv[0][index + 1])
    outputs = {k: [min(v), max(v)] for k, v in tmp_dict.iteritems()}
    fractions = float(0)
    denominator = float(0)
    for key, value in inference.iteritems():
        fractions += (float(outputs[key][0]) + float(outputs[key][1])) / 2 * value
        denominator += float(value)
    weight = round(fractions / denominator)
    return int(weight)


def fuzzy_algorithm(input1, input2, element1, element2):
    start_time = datetime.now()

    fuzzy_element1 = get_membership(element1, input1)
    fuzzy_element2 = get_membership(element2, input2)
    rule_base = read_csv_file_to_list('rule.csv')
    weight = fuzzy_defuzzification(fuzzy_inference(fuzzy_element1, fuzzy_element2, rule_base))

    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    # print("Elapsed Time :" + str(elapsed_time))
    return weight
