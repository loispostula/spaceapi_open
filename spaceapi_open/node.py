#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import json

import os
import sys


def get_nodes(places, all):
    try:
        file = open(os.path.join(os.getenv('HOME'), '.spaceapi_node'))
    except:
        print("You need to have a file .spaceapi in your homedir, with the spaceapi encoded as json")
        sys.exit()
    data = json.load(file)
    nodes = {}
    for node in data['nodes']:
        if all or node['slug'] in places:
            nodes[node['slug']] = {'url': node['url'], 'pp': node['pp']}
    return nodes