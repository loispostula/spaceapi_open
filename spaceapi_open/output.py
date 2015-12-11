#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import sys

CSI = "\x1B["
reset = CSI + "m"
reload(sys)
sys.setdefaultencoding('utf8')

def is_open(node):
    try:
        space = requests.get(node['url']).json()
    except:
        space = {}
    is_open = space.get('state', {}).get('open', None)
    try:
        people_now_present = space['sensors']['people_now_present'][0]['names']
    except:
        people_now_present = []
    return is_open, people_now_present


def out_open(node, is_o):
    out = ""
    if is_o:
        out += "#[fg=green]"
    else:
        out += "#[fg=red]"
    out += "%s%s" % ("•", "#[fg=white]")
    return out


def make(nodes, is_list):
    if is_list:
        out = ""
        for n in nodes:
            node_info = is_open(nodes[n])
            out += "%s: %s :\n" % (nodes[n]['pp'], out_open(nodes[n], node_info[0]))
            if node_info[1]:
                for people in node_info[1]:
                    out += people + '\n'


    else:
        out = ""
        for n in nodes:
            node_info = is_open(nodes[n])
            out += "%s: %s " % (nodes[n]['pp'], out_open(nodes[n], node_info[0]))
    print(out)
