'''A 2D map (list of lists) that takes a mapping (dict) name->factory for multiple layers.'''
class LayeredListOfLists(list):

    def __init__(self, size, layers={}):
        list.__init__(self)
        self.size = size

        for layer in layers:
            self.__setattr__(layer, list())

        y_max, x_max = size
        for y in range(y_max):
            self.append(list())
            for layer in layers:
                getattr(self, layer).append(list())
            for x in range(x_max):
                container = dict()
                for layer, cls in layers.items():
                    new = cls() if cls in (list, dict) else cls(y, x)
                    container[layer] = new
                    getattr(self, layer)[-1].append(new)
                self[-1].append(container)
