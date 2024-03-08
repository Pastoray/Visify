from flask import Blueprint, render_template, session, request, redirect

linked_lists_bp = Blueprint("linked_lists", __name__)

@linked_lists_bp.route("/singly/submit", methods=["POST"])
def submit_singly_linked_list():
    nodes = request.form["singly_linked_list_input"]
    return submit_linked_list(nodes ,doubly=False)

@linked_lists_bp.route("/doubly/submit", methods=["POST"])
def submit_doubly_linked_list():
    nodes = request.form["doubly_linked_list_input"]
    return submit_linked_list(nodes, doubly=True)

def submit_linked_list(nodes, doubly):
    if nodes.startswith("["):
        nodes = nodes[1:]
    if nodes.endswith("]"):
        nodes = nodes[:len(nodes) - 1]

    nodes = nodes.split(",")
    new_nodes = []
    for node in nodes:
        n = node.strip()
        if n.lower() == "null" or n.lower() == "none" or n == "":
            continue
        else:
            new_nodes.append(n)
    session["nodes"] = new_nodes

    if doubly:
        return redirect("/linked-lists/doubly/draw")
    else:
        return redirect("/linked-lists/singly/draw")

@linked_lists_bp.route("/singly/draw")
def draw_singly_linked_list():
    nodes = session.get("nodes", [])
    return render_template("draw_singly_linked_list.html", nodes=nodes)

@linked_lists_bp.route("/doubly/draw")
def draw_doubly_linked_list():
    nodes = session.get("nodes", [])
    return render_template("draw_doubly_linked_list.html", nodes=nodes)

