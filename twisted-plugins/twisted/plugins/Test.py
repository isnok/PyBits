from zope.interface import classProvides
from twisted.plugin import IPlugin

from Interfaces import IMyInterface
from Interfaces import IMyOtherInterface

class PluginOne:
    classProvides(IPlugin, IMyInterface)

class PluginTwo:
    classProvides(IPlugin, IMyOtherInterface)
