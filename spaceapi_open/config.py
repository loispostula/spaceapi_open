import argparse


class Config:
    def __init__(self):
        self._args = self._parse_args()

    def _parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--all',
                            action='store_true',
                            help="Return value for all registered spaceapi node")
        parser.add_argument('-l', '--list',
                            action='store_true',
                            help='Return list of people present at the mentionned spaceapi node')
        parser.add_argument('-r', '--refresh',
                            help='Refresh rate, default: 30')
        parser.add_argument('place', nargs='*')
        return vars(parser.parse_args())

    def get(self, key, default=None):
        val = self._args.get(key)
        if not val:
            return default
        return val