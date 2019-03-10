import time

def BT(node,N,is_visited,un_visited):
    #如果所有变量已经赋值，返回结果
    if len(is_visited) >= N:
        return node
    #取出未赋值的变量集合中第一个变量
    new_x = un_visited.pop(0)
    #遍历所有取值范围
    for i in range(N):
        new_y = i
        #约束性检查
        constraintsOK = True
        for k in range(len(is_visited)):
            x = is_visited[k].solution[0]
            y = is_visited[k].solution[1]
            #如果不满足，则将条件设为False
            if x == new_x or y == new_y or (abs(x - new_x) == abs(y - new_y)):
                constraintsOK = False
                break
        #如果满足约束性条件，进行下一步
        if constraintsOK == True:
            newNode = Queen(new_x,new_y,N,node) #创建新结点
            is_visited.append(newNode) #将该节点加入访问队列
            #如果所有变量已经被赋值，返回结果
            if len(is_visited) >= N:
                return newNode
            #递归调用下一层
            dstNode = BT(newNode,N,is_visited,un_visited)
            #找到解，返回上一级
            if dstNode != None:
                return dstNode
            #恢复访问队列
            is_visited.pop(-1)
    #恢复未访问队列
    un_visited.insert(0,new_x)
    return None

#开始递归调用BT函数
def start_BT(N):

    for i in range(N):
        start_node = Queen(0,i,N,None) #初始化起点
        is_visited = [] #存储已经访问的结点
        is_visited.append(start_node)  
        un_visited = [x for x in range(N)] #存储未访问的变量，元素为变量序号
        un_visited.remove(0) #0已经访问，去除0号元素
        dst_node = BT(start_node,N,is_visited,un_visited)  #调用BT函数
        #如果找到解，直接返回
        if dst_node != None:
            return dst_node

    return None

class Queen():
    def __init__(self,x,y,N,parent):
        # self.domain = [x for x in range(N)]
        self.index = x  #变量的序号
        self.solution = (x,y) #变量在棋盘的位置
        self.parent = parent  #变量的上一个父结点

def main():
    N = int(input('Please input N = '))
    start = time.clock()
    dst_node = start_BT(N)

    if dst_node == None:
        print("No solution")
    else:
        solution = []
        while dst_node:
            solution.append(dst_node.solution)
            dst_node = dst_node.parent
        solution = list(reversed(solution))
        print("Solution:  ",solution)

    end = time.clock()
    print("Backtracking run time : ",float(end - start),' s')

    queen_map = []
    for i in range(N):
        tmp = ['.'] * N
        queen_map.append(tmp)
    for i in range(len(solution)):
        queen_map[solution[i][0]][solution[i][1]] = 'X'

    for i in range(N):
        print(' ', ' '.join(queen_map[i]))


if __name__ == '__main__':
    main()