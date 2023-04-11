# Author 臧成龙
# coding=utf-8
# @Time    : 2022/5/16 21:09
# @File    : list_to_tree.py
# @Software: PyCharm
# @qq: 939589097

def add_node(p, node):
    # ⼦节点list
    p["children"] = []
    for n in node:
        if n.get("parent_id") == p.get("id"):
            p["children"].append(n)
    # 递归⼦节点，查找⼦节点的节点
    for t in p["children"]:
        if not t.get("children"):
            t["children"] = []
        t["children"].append(add_node(t, node))
    # 退出递归的条件
    if len(p["children"]) == 0:
        p.pop('children')
        p["choice"] = 1
        return


def list_to_route(data):
    root = []
    node = []
    # 初始化数据，获取根节点和其他子节点list
    for d in data:
        d['meta'] = {
            'title': d.pop('title'),
            'ignoreKeepAlive': d.pop('keepalive'),
            'orderNo': d.pop('sort'),
            'hideMenu': d.pop('hide_menu'),
            'icon': d.pop('icon')
        }

        d["choice"] = 0
        if d.get("parent_id") is None:
            root.append(d)
        else:
            node.append(d)
    # print("root----",root)
    # print("node----",node)
    # 查找子节点
    for p in root:
        add_node(p, node)
    # 无子节点
    if len(root) == 0:
        return node

    return root


def list_to_tree(data):
    root = []
    node = []
    # 初始化数据，获取根节点和其他子节点list

    for d in data:
        d["choice"] = 0
        if d.get("parent_id") is None:
            root.append(d)
        else:
            node.append(d)
    # print("root----",root)
    # print("node----",node)
    # 查找子节点
    for p in root:
        add_node(p, node)
    # 无子节点
    if len(root) == 0:
        return node

    return root
