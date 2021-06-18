import sys

class Constant:
    airports = [
        {'start': "ISB",'end': "LHR",'cost': 1000},
        {'start': "LHR",'end': "NYC",'cost': 750},
        {'start': "CBS",'end': "NYC",'cost': 775},
        {'start': "ISB",'end': "CBS",'cost': 575},
        {'start': "CBS",'end': "GRC",'cost': 731},
        {'start': "NYC",'end': "GRC",'cost': 459}]

class Dijkstra:

    def graphgen(data):
        graph = dict()
        for i in data:
            if i.get("start") not in graph.keys():
                graph[i.get("start")] = {i.get("end"): i.get("cost")}
            else:
                graph[i.get("start")].update({i.get("end"): i.get("cost")})

            if i.get("end") not in graph.keys():
                graph[i.get("end")] = {i.get("start"): i.get("cost")}
            else:
                graph[i.get("end")].update({i.get("start"): i.get("cost")})

        return graph

    def Shortest_path(graph, initial: str, dest: str):
        # shortest path
        path = {}
        # neighbouring nodes
        adj_node = {}
        # Queue for manipulation; adding city names only.
        queue = []
        # Check all nodes and initialize path with 0
        for node in graph:
            path[node] = float("inf")
            adj_node[node] = None
            queue.append(node)

        path[initial] = 0 #src city is distanced 0m

        # Check visited nodes and also to find the minimum distance between the nodes.
        while queue:
            key_min = queue[0]
            min_val = path[key_min]
            for n in range(1, len(queue)):
                if path[queue[n]] < min_val:
                    key_min = queue[n]
                    min_val = path[key_min]
            cur = key_min
            queue.remove(cur)

            #calculating path from the 'cur' reference
            for i in graph[cur]:
                alternate = graph[cur][i] + path[cur]
                if path[i] > alternate:
                    path[i] = alternate
                    adj_node[i] = cur
        return path.get(dest), adj_node

    def Prnt(initial, final, adj=None):    # Finally, print nodes that satisfies the condition
        temp = list()
        print(f'Shortest route between {initial} to {final}')
        if adj == None:
            temp = [initial, final]
            return (temp)
        while (adj):
            temp.append(final)
            final = adj[final]
            if final is None:
                temp.reverse()
                return(temp)


def main():

    params = sys.argv[1:]

    cost = None
    adj = None
    start = params[0]
    final = params[1]
    for ent in Constant.airports: #this code block is designed to avoid the processing if the user picked one of the dataset entity.
        if (ent['start'] == start and ent['end'] == final):
            cost = ent['cost']
    if cost is None:
        cost, adj = Dijkstra.Shortest_path(Dijkstra.graphgen(Constant.airports), start, final)
    path = Dijkstra.Prnt(start, final, adj)

    print (f'COST: {cost}, PATH FOLLOWED: {path}')

if (__name__=='__main__'):
    main()