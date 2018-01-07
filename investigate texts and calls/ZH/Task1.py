
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def count_numbers(source):
    target = []
    for i in range(len(source)):
            if source[i][0] not in target:
                target.append(source[i][0])
                if source[i][1] not in target:
                    target.append(source[i][1])
    return target
print (len(count_numbers(calls)+len(count_numbers(texts))

    
"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records.""""
