# -- coding: utf-8 --
"""
@Project: SATDemo
@Time : 2022/4/10 19:47
@Author : Yang xu
@Site : 
@File : encode.py
@IDE: PyCharm
"""


# input data
inputData = []
for line in open("input.txt", "r"):
# for line in open("input20.txt", "r"):
    inputData.append(line[:-1])

inputData[1] = '2' + inputData[1][1:]  # 小人在入口
print(inputData)

# encode
n = int(inputData[0])
step = n + n-1
cnfData = []
x = 0
v = [0, 1, 2]  # cell的状态
count = 0  # 每个cell有3个转态，切换一个cell变量编号需要加3

record = ""

for k in range(step):  # n + n-1步就能完成
    for i in range(n):  # 行
        for j in range(n):  # 列
            cellIdx = k*(n*n) + i*n + j  # 步数，行数， 列数 都从0开始
            idx = cellIdx*4  # 状态数3个, action数1个，总共4个，所以每个cell有4个编号
            check = int(inputData[i + 1][j])
            if k == 0:  # 初始状态约束
                if check == 0:  # (i*10+j)*3) 为了增加状态数变量编号
                    cnfData.append([(idx+1), 0])  # 0
                    cnfData.append([0-(idx+2), 0])  # 1
                    cnfData.append([0-(idx+3), 0])  # 2
                elif check == 1:
                    cnfData.append([0 - (idx+1), 0])  # 0
                    cnfData.append([(idx+2), 0])  # 1
                    cnfData.append([0 - (idx+3), 0])  # 2
                elif check == 2:
                    cnfData.append([0 - (idx+1), 0])  # 0
                    cnfData.append([0 - (idx+2), 0])  # 1
                    cnfData.append([(idx+3), 0])  # 2

            # 不管第几步，第几个时刻，1的地方都不会变
            if check == 1:
                cnfData.append([0 - (idx + 1), 0])  # 0
                cnfData.append([(idx + 2), 0])  # 1
                cnfData.append([0 - (idx + 3), 0])  # 2

            # elif k == step-1:  # 初始状态约束
            #     check = int(inputData1[i + 1][j])
            #     if check == 0:  # (i*10+j)*3) 为了增加状态数变量编号
            #         cnfData.append([(idx+1), 0])  # 0
            #         cnfData.append([0-(idx+2), 0])  # 1
            #         cnfData.append([0-(idx+3), 0])  # 2
            #     elif check == 1:
            #         cnfData.append([0 - (idx+1), 0])  # 0
            #         cnfData.append([(idx+2), 0])  # 1
            #         cnfData.append([0 - (idx+3), 0])  # 2
            #     elif check == 2:
            #         cnfData.append([0 - (idx+1), 0])  # 0
            #         cnfData.append([0 - (idx+2), 0])  # 1
            #         cnfData.append([(idx+3), 0])  # 2

            record += str(idx + 3) + " "  # 记录小人走过的cell编号

            # 每个cell至少一个状态
            cnfData.append([(idx+1), (idx+2), (idx+3), 0])  # 析取
            # 每个cell至多一个状态
            cnfData.append([0 - (idx+1), 0 - (idx+2), 0])  # 两两取反析取
            cnfData.append([0 - (idx+1), 0 - (idx+3), 0])  # 两两取反析取
            cnfData.append([0 - (idx+2), 0 - (idx+3), 0])  # 两两取反析取
            # action  idx+4表示发生action， idx+3表示第二个状态，小人在这个cell。即一个action的充分条件。
            if k > 0:
                cellIdx_t1 = (k - 1) * (n * n) + i * n + j  #
                cellIdx_t2 = k * (n * n) + i * n + j  #
                cnfData.append([0-(cellIdx_t1*4+4), cellIdx_t1*4+1, 0])  # 如果这个action成功发生，那么(i,j)这个cell=2就会是真
                cnfData.append([0-(cellIdx_t1*4+4), cellIdx_t2*4+3, 0])
            # action 必要条件 多个析取式合取
            # 先考虑上和左
            # if i < 1 and j < 1: # 左上角第一个
            #     cellIdx_lower = k * (n*n) + (i+1) * n + j
            #     cellIdx_right = k * (n * n) + i * n + j + 1
            #     cnfData.append([0 - (idx + 4), cellIdx_lower * 4 + 3, cellIdx_right * 4 + 3, 0])
            #     # continue
            # elif i < 1 and j >=n-1: # 右上角第一个
            #     cellIdx_left = k * (n*n) + (i+1) * n + j
            #     cellIdx_lower = k * (n * n) + i * n + j + 1
            #     cnfData.append([0 - (idx + 4), cellIdx_lower * 4 + 3, cellIdx_left * 4 + 3, 0])
            # elif i >= n-1 and j < 1: # 左下角第一个
            #     cellIdx_upper = k * (n*n) + (i+1) * n + j
            #     cellIdx_right = k * (n * n) + i * n + j + 1
            #     cnfData.append([0 - (idx + 4), cellIdx_upper * 4 + 3, cellIdx_right * 4 + 3, 0])
            # elif i >=n-1 and j >=n-1: # 右下角第一个
            #     cellIdx_upper = k * (n*n) + (i+1) * n + j
            #     cellIdx_left = k * (n * n) + i * n + j + 1
            #     cnfData.append([0 - (idx + 4), cellIdx_upper * 4 + 3, cellIdx_left * 4 + 3, 0])
            # elif i<1 and j>=1 and j<n-1: # 上边缘
            #     cellIdx_lower = k * (n * n) + (i + 1) * n + j
            #     cellIdx_left = k * (n * n) + i * n + j - 1
            #     cellIdx_right = k * (n * n) + i * n + j + 1
            #     cnfData.append([0-(idx+4), cellIdx_left * 4 + 3, cellIdx_lower*4+3, cellIdx_right*4+3, 0])
            #     # cnfData.append([0 - (idx + 4), cellIdx_left * 4 + 3, 0])
            # elif j<1 and i>=1 and i<n-1:  # 左边缘
            #     cellIdx_upper = k * (n*n) + (i-1) * n + j
            #     cellIdx_lower = k * (n * n) + (i + 1) * n + j
            #     cellIdx_right = k * (n * n) + i * n + j + 1
            #     cnfData.append([0 - (idx + 4), cellIdx_upper * 4 + 3, cellIdx_lower*4+3, cellIdx_right*4+3, 0])
            # elif i>=n-1 and j>=1 and j<n-1:  # 下边缘
            #     cellIdx_upper = k * (n * n) + (i - 1) * n + j
            #     cellIdx_left = k * (n * n) + i * n + j - 1
            #     cellIdx_right = k * (n * n) + i * n + j + 1
            #     cnfData.append([0 - (idx + 4), cellIdx_upper * 4 + 3, cellIdx_left * 4 + 3, cellIdx_right * 4 + 3, 0])
            # elif j>=n-1 and i>=1 and i<n-1:  # 右边缘
            #     cellIdx_upper = k * (n * n) + (i - 1) * n + j
            #     cellIdx_lower = k * (n * n) + (i + 1) * n + j
            #     cellIdx_left = k * (n * n) + i * n + j - 1
            #     cnfData.append([0 - (idx + 4), cellIdx_upper * 4 + 3, cellIdx_left * 4 + 3, cellIdx_lower * 4 + 3, 0])
            # else:  # 内部的
            #     # cellIdx1 = k * (n*n) + i * n + j - 1  # 左边cell
            #     # cellIdx2 = k * (n*n) + (i-1) * n + j  # 上边cell
            #     # # 上边，左边至少一个状态是2
            #     # cnfData.append([0-(idx+4), cellIdx1*4 + 3, cellIdx2 * 4 + 3, 0])
            #     # # 当前这个cell必须是0，下面不需要加入cell状态不为1的文字，因为上面有约束定义了，一个cell一个时刻只能有一个状态
            #     # cnfData.append([0 - (idx+4), idx+1, 0])
            #     cellIdx_upper = k * (n * n) + (i - 1) * n + j
            #     cellIdx_lower = k * (n * n) + (i + 1) * n + j
            #     cellIdx_left = k * (n * n) + i * n + j - 1
            #     cellIdx_right = k * (n * n) + i * n + j + 1
            #     cnfData.append([0 - (idx + 4), cellIdx_upper * 4 + 3, cellIdx_lower * 4 + 3, cellIdx_left * 4 + 3, cellIdx_lower * 4 + 3, 0])
            # cnfData.append([0 - (idx + 4), idx + 1, 0])
            # 如果两个时刻的状态不一样，0-》2，那么至少发生了一个action  a
            # action 必要条件 多个析取式合取 只考虑上和左出发
            if i < 1 and j < 1: # 左上角第一个
                continue
            elif i<1 and j>=1: # 上边缘
                cellIdx_left = k * (n * n) + i * n + j - 1
                cnfData.append([0 - (idx + 4), cellIdx_left * 4 + 3, 0])
                cnfData.append([0 - (idx + 4), idx + 1, 0])
            elif j<1 and i>=1:  # 左边缘
                cellIdx_upper = k * (n*n) + (i-1) * n + j
                cnfData.append([0 - (idx + 4), cellIdx_upper * 4 + 3, 0])
                cnfData.append([0 - (idx + 4), idx + 1, 0])
            else:  # 内部的
                cellIdx_left = k * (n*n) + i * n + j - 1  # 左边cell
                cellIdx_upper = k * (n*n) + (i-1) * n + j  # 上边cell
                # 上边，左边至少一个状态是2
                cnfData.append([0-(idx+4), cellIdx_left*4 + 3, cellIdx_upper * 4 + 3, 0])
                # 当前这个cell必须是0，下面不需要加入cell状态不为1的文字，因为上面有约束定义了，一个cell一个时刻只能有一个状态
                cnfData.append([0 - (idx+4), idx+1, 0])

            # 时序约束
            if k > 0:
                cellIdx_t1 = (k-1) * (n*n) + i * n + j  #
                cellIdx_t2 = k * (n*n) + i * n + j  #
                cnfData.append([cellIdx_t1*4+3, 0 - (cellIdx_t2*4+3), cellIdx_t1*4+4, 0])

# 目标状态约束，小人走到出口，n*n cell = 2
cnfData.append([step*n*n*4-1, 0])  # 最后一个文字是action，所以要减一

# data =[ ['a','b','c'],['a','b','c'],['a','b','c']]

with open("data.txt", "w") as f:  #设置文件对象
# with open("data20.txt", "w") as f:  # 设置文件对象
    f.write("p cnf " + str(step * n * n * 4) + " " + str(len(cnfData)) + '\n')
    for i in cnfData:  #对于双层列表中的数据
        # i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'  #将其中每一个列表规范化成字符串   '\''是转义
        i = str(i).strip('[').strip(']').replace(',', '') + '\n'
        f.write(i)
        # f.writelines(i)

with open("mayPath.txt", "w") as f:
# with open("mayPath20.txt", "w") as f:
    f.writelines(record)
