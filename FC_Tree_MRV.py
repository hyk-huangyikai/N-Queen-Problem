import time

def FCcheck(new_x,new_y,un_visited):
    # print('x,y',new_x,new_y)
    length = len(un_visited)
    for i in range(0,length):
        node = un_visited[i]
        new_domain = []
        for y in node.domain:
            x = node.index
            # print('a',x,y,new_x,new_y)
            if x == new_x or y == new_y or (abs(x - new_x) == abs(y - new_y)):
                # print("a")
                continue
            else:
                # print('b')
                new_domain.append(y)
        if len(new_domain) == 0:
            return "DWO"
        node.domain = new_domain
    # print(un_visited[1].domain,un_visited[2].domain,un_visited[3].domain)
    return True

def FC(node,N,is_visited,un_visited):

    # print('id,domain,solution',node.index,node.domain,node.solution)
    new_x = node.index
    domain = node.domain
    for i in domain:
        new_y = i
        constraintsOK = True
        for k in range(len(is_visited)):
            x = is_visited[k].solution[0]
            y = is_visited[k].solution[1]
            # print("bbb",x,y,new_x,new_y)
            if x == new_x or y == new_y or (abs(x - new_x) == abs(y - new_y)):
                constraintsOK = False
                break
        if constraintsOK == False:
            continue
        save_domain = {}
        for k in range(len(un_visited)):
            save_tmp = [x for x in un_visited[k].domain]
            save_domain[un_visited[k].index] = save_tmp

        DWOoccurred = False
        if FCcheck(new_x,new_y,un_visited) == "DWO":
            DWOoccurred = True
        # print("new:",new_x,new_y,constraintsOK,DWOoccurred)
        # print(un_visited[1].domain,un_visited[2].domain,un_visited[3].domain)
        if DWOoccurred == False:
            node.solution = (new_x,new_y)
            is_visited.append(node)
            if len(is_visited) >= N:
                return node
            min_node_index = 0
            min_domain_length = len(un_visited[0].domain)
            for k in range(len(un_visited)):
                if len(un_visited[k].domain) < min_domain_length:
                    min_node_index = k

            newNode = un_visited.pop(min_node_index)
            newNode.parent = node
            dstNode = FC(newNode,N,is_visited,un_visited)
            if dstNode != None:
                return dstNode
            is_visited.pop(-1)
            un_visited.append(newNode)
        for k in range(len(un_visited)):
            index = un_visited[k].index
            un_visited[k].domain = [x for x in save_domain[index]]

    # un_visited.insert(0,node1)
    return None


def start_FC(N):

    un_visited = []
    for i in range(N):
        newNode = Queen(i,0,N,None)
        un_visited.append(newNode)

    for i in range(N):
        start_node = Queen(0,i,N,None)
        is_visited = []
        # is_visited.append(start_node)
        un_visited.pop(0)
        dst_node = FC(start_node,N,is_visited,un_visited)
        if dst_node != None:
            return dst_node

    return None

class Queen():
    def __init__(self,x,y,N,parent):
        self.domain = [x for x in range(N)]
        self.index = x
        self.solution = (x,y)
        self.parent = parent

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
        print(' ',' '.join(queen_map[i]))

if __name__ == '__main__':
    main()