![image](https://user-images.githubusercontent.com/48397805/164372823-7f8cc347-6e4d-49df-80d9-9ba955ed547c.png)

![image](https://user-images.githubusercontent.com/48397805/164372925-8281f778-9e97-4e41-b2e9-88eeb6637ac5.png)

![image](https://user-images.githubusercontent.com/48397805/164372944-98b6e460-232e-4ddb-b267-79573c4d7bde.png)

![image](https://user-images.githubusercontent.com/48397805/164372975-a5521fde-176f-4172-ad4d-0e3f563c7e67.png)


## 2. 编码 (SAT demo的工作)

P(i,j,k)表示第i层，第j列的车位转态，k∈{0,1,2,3,4,5,6,7,8,9}。k=0表示该车位为空，k=1表示该车位已经停有车辆，k=2,3,4...,9表示该车位分配给车辆2,3,4,...,9。这里默认编号越大的车辆，越重。

### 2.1 encode.py是编码源代码

代码会随机生成一个车库停车情况map并写入input.txt，输出CNF文件cnfFile.cnf。下面块是input.txt样例

```
1 1 1 0 1 0 0 1 0 1
1 1 0 1 1 0 1 0 1 0
0 0 1 0 0 0 1 1 1 1
0 1 1 0 0 0 0 1 0 1
1 0 0 0 1 1 1 0 0 1
1 1 1 1 1 0 0 1 1 1
0 1 0 0 0 1 1 0 0 1
0 0 0 1 0 0 0 1 0 0
1 0 1 0 1 1 1 1 0 1
1 0 0 0 1 0 0 1 1 0
```

### 2.2 SAT solver 去解CNF文件

![image](https://user-images.githubusercontent.com/48397805/164376112-cf176a47-5b89-4b78-9099-edd66daa52b8.png)
SAT求解得到的解放在SATsolution.txt中

## 3. 解码

### 3.1 decode.py是解码源代码

代码读取SAT的求解结果SATsolution.txt，通过解码得到result.txt，从结果中能看出，待入库的8两车辆都集中在左下角，这是因为存取车入口在左下角。还能发现编号较大的车辆存放在下层，编号较小的车辆存放在上层，这是因为希望达到车库总体重心最低的目标。

```
1 1 1 0 1 0 0 1 0 1
1 1 0 1 1 0 1 0 1 0
0 0 1 0 0 0 1 1 1 1
0 1 1 0 0 0 0 1 0 1
1 0 0 0 1 1 1 0 0 1
1 1 1 1 1 0 0 1 1 1
0 1 0 0 0 1 1 0 0 1
2 3 0 1 0 0 0 1 0 0
1 4 1 0 1 1 1 1 0 1
1 9 7 8 1 5 6 1 1 0
```

具体的实例

![image](https://user-images.githubusercontent.com/48397805/164186178-398ef286-89a3-4df0-903c-3b956432566f.png)
