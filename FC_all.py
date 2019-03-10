import time
num = 0
queen_solution = []
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
        #结束探索的条件
        if len(cur_un_assigned) <= 0:
            global num #统计解个数
            global queen_solution #存储其中一个解
            num += 1
            #存储其中一个解，方便后面验证合法性
            if len(queen_solution) == 0:
                queen_solution = solution[:]
            #输出当前找到的解
            for i in range(N):
                print('(', i, ",", solution[i], ')', end='')
            print()
            continue
        cur_domain = []
        for k in range(N):
            tmp = domain[k][:]
            cur_domain.append(tmp)
        if FCcheck(index,value,cur_un_assigned,cur_domain) == "DWO":
            continue
        min_index = cur_un_assigned[0]
        min_length = len(cur_domain[min_index])
        for k in range(1,len(cur_un_assigned)):
            if len(cur_domain[cur_un_assigned[k]]) < min_length:
                min_length = len(cur_domain[cur_un_assigned[k]])
                min_index = cur_un_assigned[k]
        FC(cur_un_assigned,cur_domain,solution,N,min_index)


def start_FC(N):

    domain = []
    for i in range(N):
        domain.append([x for x in range(N)])

    un_assigned = [x for x in range(N)]
    solution = [0]*N

    FC(un_assigned,domain,solution,N,0)
    return solution

def main():
    N = int(input('Please input N = '))
    start = time.clock()
    print("Total solution: ")
    solution = start_FC(N)
    if solution == None:
        print("No solution")
    else:
        end = time.clock()
        print("Total solution number: ", num)
        print("Forwardchecking run time : ",float(end - start),' s')
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