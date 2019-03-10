import time

visit_state = 0

def FCcheck(index,value,cur_un_assigned,cur_domain):
    #遍历所有未赋值的变量
    for x in cur_un_assigned:
        new_domain = []
        #遍历各个取值
        for y in cur_domain[x]:
            #不符合条件，去掉该取值
            if y == value or (abs(x - index) == abs(y - value)):
                continue
            else:
                new_domain.append(y)
        #如果值域为空，返回DWO
        if len(new_domain) == 0:
            return "DWO"
        #更新值域
        cur_domain[x] = new_domain
    #更新成功
    return True

def FC(un_assigned,domain,solution,N,index):
    global visit_state
    visit_state += 1
    #另开一个未赋值变量的副本，简化后面恢复的步骤
    cur_un_assigned = un_assigned[:]
    #将准备赋值的变量移出
    cur_un_assigned.remove(index)
    #遍历所有取值
    for value in domain[index]:
        solution[index] = value #赋值
        #如果当前所有变量已经访问完，则结束探索
        if len(cur_un_assigned) <= 0:
            return True
        #备份值域，简化后面恢复的步骤
        cur_domain = []
        for k in range(N):
            tmp = domain[k][:]
            cur_domain.append(tmp)
        #FC——check检查
        if FCcheck(index,value,cur_un_assigned,cur_domain) == "DWO":
            continue
        #调用下一层FC
        result = FC(cur_un_assigned,cur_domain,solution,N,index+1)
        if result != False:
            return result

    return False


def start_FC(N):

    #二维列表表示变量的值域
    domain = []
    for i in range(N):
        domain.append([x for x in range(N)])
    #一维列表表示未赋值的变量
    un_assigned = [x for x in range(N)]
    solution = [0]*N
    #FC函数
    result = FC(un_assigned,domain,solution,N,0)

    if result == True:
        return solution
    return False

def main():
    N = int(input('Please input N = '))
    start = time.clock()
    solution = start_FC(N)

    if solution == False:
        print("No solution")
    else:
        for i in range(N):
            print('(', i, ",", solution[i], ')', end='')
        print()

    end = time.clock()
    print("Forwardchecking run time : ",float(end - start),' s')

    print("visited state number: ",visit_state)

    queen_map = []
    for i in range(N):
        tmp = ['.'] * N
        queen_map.append(tmp)
    for i in range(len(solution)):
        queen_map[i][solution[i]] = 'X'

    for i in range(N):
        print(' ', ' '.join(queen_map[i]))


if __name__ == '__main__':
    main()