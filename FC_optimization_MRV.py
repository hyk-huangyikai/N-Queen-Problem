import time
visit_state = 0

def FCcheck(index,value,cur_un_assigned,cur_domain):

    for x in cur_un_assigned:
        new_domain = []
        for y in cur_domain[x]:
            if y == value or (abs(x - index) == abs(y - value)):
                continue
            else:
                new_domain.append(y)
        if len(new_domain) == 0:
            return "DWO"
        cur_domain[x] = new_domain
    return True

def FC(un_assigned,domain,solution,N,index):
    global visit_state
    visit_state += 1
    cur_un_assigned = un_assigned[:]
    cur_un_assigned.remove(index)
    for value in domain[index]:
        solution[index] = value
        if len(cur_un_assigned) <= 0:
            return True
        cur_domain = []
        for k in range(N):
            tmp = domain[k][:]
            cur_domain.append(tmp)
        if FCcheck(index,value,cur_un_assigned,cur_domain) == "DWO":
            continue
        min_index = cur_un_assigned[0] #存储当前取值最少的变量序号
        min_length = len(cur_domain[min_index]) #存储当前取值最少的个数
        #遍历，寻找取值最少的变量序号
        for k in range(1,len(cur_un_assigned)):
            #如果取值更少，则直接更新值域长度、变量序号
            if len(cur_domain[cur_un_assigned[k]]) < min_length:
                min_length = len(cur_domain[cur_un_assigned[k]])
                min_index = cur_un_assigned[k]
        #将取值最少的变量序号作为参数传递
        result = FC(cur_un_assigned,cur_domain,solution,N,min_index)
        if result != False:
            return result

    return False


def start_FC(N):

    domain = []
    for i in range(N):
        domain.append([x for x in range(N)])

    un_assigned = [x for x in range(N)]
    solution = [0]*N

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
        print(' ', ''.join(queen_map[i]))


if __name__ == '__main__':
    main()