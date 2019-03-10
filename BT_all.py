import time
num = 0
queen_solution = []
visit_state = 0

def valid(index,queen_list):
    for k in range(0,index):
        if abs(index - k) == abs(queen_list[index] - queen_list[k]) or queen_list[index] == queen_list[k]:
            return False
    return True


def BT(index,N,queen_list):
    global visit_state
    visit_state += 1
    #如果探索到最后一个变量，结束递归
    if index >= N:
        global num
        global queen_solution #记录其中一个解，方便后面具体分析
        num += 1
        if len(queen_solution) == 0:
            queen_solution = queen_list[:]
        #输出当前找到的解
        for i in range(N):
            print('(', i, ",", queen_list[i], ')', end='')
        print()
    else:
        #遍历所有值域
        for k in range(N):
            queen_list[index] = k #变量赋值
             #检查约束合法性
            if (valid(index,queen_list)):
                #进入下一层
                BT(index+1,N,queen_list)

def main():
    N = int(input('Please input N = '))
    start = time.clock()
    queen_list = [0]*N
    print("Total solution: ")
    BT(0,N,queen_list)
    end = time.clock()
    print("Total solution number: ", num)
    print("Backtracking run time : ",float(end - start),' s')
    print("visited state number: ",visit_state)
    print("-----")
    print("One solution: ")
    queen_map = []
    for i in range(N):
        tmp = ['.'] * N
        queen_map.append(tmp)
    for i in range(len(queen_solution)):
        queen_map[i][queen_solution[i]] = 'X'

    for i in range(N):
        print(' ', ' '.join(queen_map[i]))


if __name__ == '__main__':
    main()