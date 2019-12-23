# Author: Ibrahim Sha
# ibrahim45@github

class TravellingSalesManProblem:
    data = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    node_len = len(data)
    parent_node_pos = 0

    def get_child_nodes(self, child_parent_node_pos, ele):
        child_node_len = len(ele)
        child_nodes = list(range(child_node_len))
        child_nodes.pop(child_parent_node_pos)
        return child_nodes

    def remove_parent_node(self, child_parent_node_pos, ele):
        ele.pop(child_parent_node_pos)
        return ele

    def cal_path_val(self, xnode, ynode):
        return self.data[xnode][ynode]

    def iterate_child_last(self, pos, branch_nodes):
        print("[================= branch nodes are -{0}]".format(branch_nodes))
        result = 0
        child_nodes = self.remove_parent_node(pos, branch_nodes.copy())
        print("ITERATIVE CHILD NODES ARE - {0} <============== BRANCH NODES ARE {1} and position is {2}".format(child_nodes, branch_nodes, branch_nodes[pos]))

        for index_pos_j, j in enumerate(child_nodes):
            result += self.cal_path_val(branch_nodes[pos], j) + self.iterate_child_last(index_pos_j, child_nodes)
        return  result
        
    def analyze(self):
        child_nodes = self.get_child_nodes(0, self.data)
        result = [[]] * self.node_len
        print("child node is {0}".format(child_nodes))
        for index_pos, i in enumerate(child_nodes):
            print("Index Position is {0} and current child node ----/=====child=====/\------is {1}".format(index_pos, i))
            result[i] = self.cal_path_val(self.parent_node_pos, i) + self.iterate_child_last(index_pos, child_nodes.copy())
        return result

    def output(self):
        print("The Final efficient root path is:")
        print(self.get_child_nodes(0, self.data))
        print(self.analyze())

    

tsp = TravellingSalesManProblem()
tsp.output()
