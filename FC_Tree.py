import time

def FCcheck(new_x,new_y,un_visited):
    length = len(un_visited)
    #遍历剩余变量
    for i in range(new_x+1,length):
        node = un_visited[i]
        new_domain = []
        #遍历各种取值
        for y in node.domain:
            x = node.index
            #如果不符合条件，则去除该取值
            if x == new_x or y == new_y or (abs(x - new_x) == abs(y - new_y)):
                continue
            else:
                new_domain.append(y)
        #如果值域为空，说明不能再探索，返回DWO
        if len(new_domain) == 0:
            return "DWO"
        #更新值域
        node.domain = new_domain
    #更新成功
    return True

def FC(node,N,is_visited,un_visited):


    new_x = node.index #变量的序号
    domain = node.domain #变量的值域
    #探索所有值域
    for i in domain:
        new_y = i
        #约束性条件检查
        constraintsOK = True
        for k in range(len(is_visited)):
            x = is_visited[k].solution[0]
            y = is_visited[k].solution[1]
            #如果在同一行、同一列或同一斜方向，不符合条件
            if x == new_x or y == new_y or (abs(x - new_x) == abs(y - new_y)):
                constraintsOK = False
                break
        if constraintsOK == False:
            continue
        #将所有变量的值域保存备份
        save_domain = []
        for i in range(len(un_visited)):
            save_tmp = [x for x in un_visited[i].domain]
            save_domain.append(save_tmp)
        #检查更新剩余未访问的变量的值域
        DWOoccurred = False
        if FCcheck(new_x,new_y,un_visited) == "DWO":
            DWOoccurred = True
        
        if DWOoccurred == False:
            node.solution = (new_x,new_y) #确定变量的位置
            is_visited.append(node) #添加变量到已访问的列表中
            #如果变量已经全部赋值，返回结果
            if len(is_visited) >= N:
                return node
            #要探索的新结点
            newNode = un_visited[new_x+1]
            newNode.parent = node
            #递归调用下一层
            dstNode = FC(newNode,N,is_visited,un_visited)
            #找到解直接返回上一级
            if dstNode != None:
                return dstNode
            #恢复访问的列表
            is_visited.pop(-1)
        #恢复未访问的变量之前的值域
        for i in range(len(save_domain)):
            un_visited[i].domain = [x for x in save_domain[i]]

    return None


def start_FC(N):
    #初始化为赋值的点的集合
    un_visited = []
    for i in range(N):
        newNode = Queen(i,0,N,None)
        un_visited.append(newNode)
    #从第一个结点开始    
    for i in range(N):
        start_node = Queen(0,i,N,None) #初始化第一个结点
        is_visited = [] #初始化已赋值的列表
        #调用FC函数
        dst_node = FC(start_node,N,is_visited,un_visited) 
        #找到解返回结果
        if dst_node != None:
            return dst_node

    return None

#类结点存储结点状态
class Queen():
    def __init__(self,x,y,N,parent):
        self.domain = [x for x in range(N)] #变量的域
        self.index = x #变量的序号
        self.solution = (x,y) #变量在棋盘的位置
        self.parent = parent #变量的上一个父母状态

def main():
    N = int(input('Please input N = '))
    start = time.clock()
    dst_node = start_FC(N)

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
    print("Forwardchecking run time : ",float(end - start),' s')

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