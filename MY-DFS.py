class DFS:

    def __init__(self, states, initial, goal):
        self.states = states
        self.goal = goal
        self.frontiers = [[initial,]]
        self.explored = []
        try:
            self.search()
        except:
            print('The DFS search fails')


    def end(self, result, path=None):
        if result==True:    
            detailed_path = ''
            for state in path:
                detailed_path += state + ' ==> '
            detailed_path = detailed_path[:-5]
            print('The DFS search succeeds, The path is:  ' + detailed_path)
        else:
            print('The DFS search fails')


    def search(self):
        while self.frontiers != []:
            path = self.frontiers.pop(-1)
            state = path[-1]
            self.explored.append(state)
            if state == self.goal:
                return self.end(True, path)
            for state in self.states[state]:
                new_path = list(path)
                new_path.append(state)
                if state not in self.explored and  path not in self.frontiers:
                    self.frontiers.append(new_path)
        return self.end(False)








if __name__ == '__main__':
    states = {
                'A': ['Z', 'S', 'T'],
                'Z': ['O', 'A'],
                'O': ['Z', 'S'],
                'S': ['A', 'O', 'R', 'F'],
                'T': ['A', 'L'],
                'L': ['T', 'M'],
                'M': ['L', 'D'],
                'D': ['M', 'C'],
                'C': ['D', 'R', 'P'],
                'R': ['S', 'C', 'P'],
                'P': ['R', 'C', 'B'],
                'F': ['S', 'B'],
                'B': ['G', 'U', 'F', 'P'],
                'G': ['B'],
                'U': ['V', 'H', 'B'],
                'H': ['U', 'E'],
                'E': ['H'],
                'V': ['U', 'I'],
                'I': ['V', 'N'],
                'N': ['I'],
    }
    initial = 'A'
    goal = 'B'

    DFS(states, initial, goal)