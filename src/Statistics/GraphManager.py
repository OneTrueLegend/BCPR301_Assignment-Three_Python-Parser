from src.Statistics.AbstractGraph import AbstractGraph


class GraphManager(object):
    def __init__(self, graph_type):
        self.graph_type = graph_type

    def make_graph(self, class_data_list):
        if isinstance(self.graph_type, AbstractGraph):
            self.graph_type.initialize()
            self.graph_type.insert(class_data_list)
            self.graph_type.finalize()
        else:
            print('no such graph type')
