from zope.interface import Interface

class IMyInterface(Interface):
    """ An interface to find plugins. """

class IMyOtherInterface(IMyInterface):
    """ Another plugin finder interface. """
