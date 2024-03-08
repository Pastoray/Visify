from flask import Blueprint, render_template, session, request, redirect
from collections import deque

trees_bp = Blueprint("trees", __name__)

@trees_bp.route("/submit", methods=["POST"])
def submit_tree():
    nodes = request.form["tree_input"]
    if nodes.startswith("["):
        nodes = nodes[1:]
    if nodes.endswith("]"):
        nodes = nodes[:len(nodes) - 1]

    nodes = deque(nodes.split(","))

    new_nodes = []
    power = 0
    while nodes:
        tmp = []
        while len(tmp) < (2 ** power):
            if new_nodes and new_nodes[-1][len(tmp) // 2] == None:
                tmp.append(None)
                continue
            node = nodes.popleft() if nodes else None
            if node == None or node.strip() == "" or node.strip().lower() == "null" or node.strip().lower() == "none":
                tmp.append(None)
            else:
                tmp.append(node.strip())
        new_nodes.append(tmp)
        power += 1

    session["nodes"] = new_nodes

    return redirect("/trees/draw")

@trees_bp.route("/draw")
def draw_tree():
    nodes = session.get("nodes", [])
    return render_template("draw_tree.html", nodes=nodes)
