#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import argparse


class Config:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._args = self._parse_args()

    def _parse_args(self):
        self.parser.add_argument('-a', '--all',
                            action='store_true',
                            help="Return value for all registered spaceapi node")
        self.parser.add_argument('-l', '--list',
                            action='store_true',
                            help='Return list of people present at the mentionned spaceapi node')
        self.parser.add_argument('-r', '--refresh',
                            help='Refresh rate, default: 30')
        self.parser.add_argument('place', nargs='*')
        return vars(self.parser.parse_args())

    def print_help(self):
        self.parser.print_usage()

    def get(self, key, default=None):
        val = self._args[key]
        return val