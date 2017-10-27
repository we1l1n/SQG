import numpy as np


class Path(list):
    def __init__(self, *args):
        super(Path, self).__init__(*args)

    @property
    def confidence(self):
        return np.prod([edge.confidence for edge in self])

    def replace_edge(self, old_edge, new_edge):
        try:
            new_path = Path(self)
            new_path[new_path.index(old_edge)] = new_edge
            return new_path
        except ValueError:
            return None
