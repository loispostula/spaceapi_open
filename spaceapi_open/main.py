#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys

from spaceapi_open import config
from spaceapi_open import node
from spaceapi_open import output


def main():
    conf = config.Config()
    if not all and not conf.get("place"):
        conf.print_help()
        sys.exit(0)
    nodes = node.get_nodes(conf.get("place"), conf.get("all"))
    output.make(nodes, conf.get("list"))

if __name__ == '__main__':
    main()