import time
visit_state = 0

#约束性检查
def valid(index,queen_list):
    #检查前面已经赋值的变量
    for k in range(0,index):
        #如果在同一列，或者同一条斜线，返回False
        if abs(index - k) == abs(queen_list[index] - queen_list[k]) or queen_list[index] == queen_list[k]:
            return False
    #合法则返回True
    return True


def BT(index,N,queen_list):
    global visit_state
    visit_state += 1
    #如果探索到最后一个变量，结束递归
    if index >= N:
        return True
    else:
        #遍历所有值域
        for k in range(N):
            queen_list[index] = k #为当前变量赋值
            #检查约束合法性
            if (valid(index,queen_list)):
                #进入下一层，如果返回True，说明找到解，继续返回上一级
                if BT(index+1,N,queen_list) == True:
                    return True
    #找不到解，返回False给上一级
    return False

def main():
    N = int(input('Please input N = '))
    start = time.clock()
    queen_list = [0]*N
    result = BT(0,N,queen_list)
    if result == False:
        print("No solution")
    else:
        for i in range(N):
            print('(', i, ",", queen_list[i], ')', end='')
        print()

    end = time.clock()
    print("Backtracking run time : ",float(end - start),' s')

    print("visited state number: ",visit_state)

    queen_map = []
    for i in range(N):
        tmp = ['.'] * N
        queen_map.append(tmp)
    for i in range(len(queen_list)):
        queen_map[i][queen_list[i]] = 'X'

    for i in range(N):
        print(' ', ' '.join(queen_map[i]))


if __name__ == '__main__':
    main()