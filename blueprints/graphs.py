from flask import Blueprint, render_template, session, request, redirect
import re

graphs_bp = Blueprint("graphs", __name__)

@graphs_bp.route("graph-map/submit", methods=["POST"])
def graph_map():
    nodes = request.form["graph_map_input"]
    arr = []
    graph = get_graph_map_partitions(nodes)
    for key in graph:
        for value in graph[key]:
            arr.append([key, value])
    
    return make_graph(arr)

@graphs_bp.route("graph-array/submit", methods=["POST"])
def graph_array():
    nodes = request.form["graph_array_input"]
    arr = get_graph_array_partitions(nodes)

    return make_graph(arr)

def make_graph(arr):
    graph = {}
    
    nodes_set = set()
    for i in range(len(arr)):
        frm = arr[i][0].strip()
        to = arr[i][1].strip()
        nodes_set.add(frm)
        nodes_set.add(to)
        if frm in graph:
            graph[frm].append(to)
        else:
            graph[frm] = [to]
    
    def dfs(curr_node, curr_seen, starting_node, level):
        curr_seen.add(curr_node)
        nonlocal global_level
        for child in graph.get(curr_node, []):
            global_seen.add(child)
            global_level = max(global_level, level)
            if child not in curr_seen:
                if level in graphs[-1]:
                    graphs[-1][level].append([[], child, 1])
                else:
                    graphs[-1][level] = [[[], child, 1]]

                dfs(child, curr_seen, starting_node, level + 8)

    graphs = []
    global_seen = set()
    global_level = 0

    height = (len(nodes_set)) * 2 + 1
    
    for starting_node in graph:
        if starting_node not in global_seen:
            global_level += 8
            graphs.append({})
            graphs[-1][global_level] = [[[], starting_node, height // 2]]
            dfs(starting_node, set(), starting_node, global_level + 8)

    for i in range(len(graphs)):
        for l in graphs[i]:
            level_nodes = len(graphs[i][l])
            step = (((height - level_nodes) // (level_nodes + 1) + 1))
            for j in range(len(graphs[i][l])):
                graphs[i][l][j][2] = step * (j + 1)

    for i in range(len(graphs)):
        for l in graphs[i]:
            for j in range(len(graphs[i][l])):
                if l - 8 in graphs[i]:
                    for nd in graphs[i][l - 8]:
                        if nd[1] in graph and graphs[i][l][j][1] in graph[nd[1]]:
                            graphs[i][l][j][0].append(nd[2])

    width = max(graphs[-1].keys()) + 2

    graphs.append(height)
    graphs.append(width)
    session["nodes"] = graphs
    
    return redirect("/graphs/graph/draw")

@graphs_bp.route("/graph/draw")
def draw_graph():
    nodes = session.get("nodes", [])
    width = nodes.pop()
    height = nodes.pop()
    return render_template("draw_graph.html", nodes=nodes, height=height, width=width)

def get_graph_array_partitions(string):
    pattern = re.compile(r'\[([^,\[\]]*?),([^,\[\]]*?)\]')
    partitions = pattern.findall(string)
    return partitions

def get_graph_map_partitions(string):
    pattern = re.compile(r'(\w+):\s*\[([^\]]+)\]')
    partitions = pattern.findall(string)
    graph_map = {}
    for key, value in partitions:
        graph_map[key] = [item.strip() for item in value.split(',')]
    return graph_map

