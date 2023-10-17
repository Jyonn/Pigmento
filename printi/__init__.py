from .plugins import LogPlugin, BasePlugin
from .utils import Prefix, Color, Bracket

from .time_prefix import TimePrefix
from .printi import Printi

prt = Printi()


def add_time_prefix(bracket=Bracket.DEFAULT, color=Color.GREEN):
    prt.add_prefix(Prefix(TimePrefix(), bracket, color))


def add_log_plugin(log_file):
    prt.add_plugin(LogPlugin(log_file))
