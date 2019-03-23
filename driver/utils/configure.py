from ast import literal_eval
from argparse import Namespace
import pprint


class Configure(Namespace):

    def __init__(self, config):
        with open("configs/"+config, "r") as fp:
            configs = literal_eval(fp.read())
        self.printconfig(configs)
        Namespace.__init__(self, **configs)
        self.platformName = self.desiredCaps['platformName']

    def printconfig(self, configs):
        self.log(pprint.pformat(configs))
