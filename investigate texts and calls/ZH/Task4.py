
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
def seller_numbers(source):
    sellers = set()   #建立集合
    a_calls = set()   #接电话集合
    for i in range(len(source)):
        a_calls.add(source[i][1])
        if source[i][0] not in a_calls:
            sellers.add(source[i][0])
    return sellers
seller_a = seller_numbers(calls)
def seller_eli(source):
    for i in range(len(source)):
        if source[i][0] in seller_a:
            seller_a.remove(source[i][0])
            if source[i][1] in seller_a:
                seller_a.remove(source[i][1])
    return seller_a
seller_final = "\n".join(seller_eli(texts))
print ('These numbers could be telemarketers:' + '\n' + seller_final)
        

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

