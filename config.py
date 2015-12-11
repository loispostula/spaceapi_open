import argparse


class Config:
    def __init__(self):
        self._args = self._parse_args()

    @staticmethod
    def _parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--all',
                            action='store_true',
                            help="Return value for all registered spaceapi node")
        parser.add_argument('-l', '--list',
                            help='Return list of people present at the mentionned spaceapi node')
        parser.add_argument('-r', '--refresh',
                            help='Refresh rate, default: 30')
        parser.add_argument('place', nargs='*')
        return vars(parser.parse_args())