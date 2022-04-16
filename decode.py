# -- coding: utf-8 --
"""
@Project: SATDemo
@Time : 2022/4/15 21:26
@Author : Yang xu
@Site : 
@File : decode.py
@IDE: PyCharm
"""

# input data
# f1 = open("solutionValue.txt", "r")

SolutionData = ""
for line in open("solutionValue.txt", "r"):
# for line in open("solutionValue20.txt", "r"):
    SolutionData += line[1:-1]

SolutionData = SolutionData.strip(' ').split(' ')
# print(SolutionData)

f2 = open("mayPath.txt", "r")
# f2 = open("mayPath20.txt", "r")
mayPathData = f2.readline().strip(' ').split(' ')
# print(mayPathData)

pathResult = []
for v in SolutionData:
    if int(v) > 0 and v in mayPathData:
        pathResult.append(v)

print(pathResult)
print(len(pathResult))

# 打印路径坐标
n = 10
# n = 20
result = []
for i, v in enumerate(pathResult):
    t = int(v)-i*n*n*4
    x = t//(n*4)  # 第几行
    y = t % (n*4) // 4  # 第几列
    result.append([x, y])
    print(x, y)

with open("result10.txt", "w") as f:
# with open("result20.txt", "w") as f:
    for i in result:
        i = str(i).strip('[').strip(']').replace(',', '') + '\n'
        f.write(i)
