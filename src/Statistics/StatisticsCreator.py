from src.Database import SQLError
from src.Statistics.BarAttributeGraph import BarAttributeGraph
from src.Statistics.BarMethodAttributeGraph import BarMethodAttributeGraph
from src.Statistics.BarMethodGraph import BarMethodGraph
from src.Statistics.ClassData import ClassData
from src.Statistics.GraphManager import GraphManager


class StatisticsCreator(object):
    def __init__(self, db):
        self.db = db

    def display_graph(self, graph_type=None):
        graph = BarMethodAttributeGraph()
        if graph_type == 'methods':
            graph = BarMethodGraph()
        elif graph_type == 'attributes':
            graph = BarAttributeGraph()
        else:
            print("Unknown graph type selected, defaulting to showing Methods and Attributes")
        print("Creating graph, please wait...")
        GraphManager(graph).make_graph(self.get_class_data())

    def create_tables(self):
        try:
            self.db.query(
                "CREATE TABLE IF NOT EXISTS ClassData (className "
                "TEXT, attributeCount INTEGER, methodCount INTEGER);")
        except SQLError as e:
            print(e)

    def insert_class(self, class_node):
        try:
            self.db.query(
                "INSERT INTO ClassData (className, attributeCount, methodCount) VALUES('{}',{},{});".format(
                    class_node.name, len(class_node.attributes),
                    len(class_node.functions)))
        except SQLError as e:
            print(e)

    def get_class_data(self):
        class_data_list = []
        try:
            result = self.db.query(
                "SELECT className,attributeCount,methodCount from ClassData").fetch()
        except SQLError as e:
            print(e)
        for row in result:
            class_name = row['className']
            attribute_count = row['attributeCount']
            method_count = row['methodCount']
            class_data_list.append(
                ClassData(
                    class_name,
                    attribute_count,
                    method_count))
        return class_data_list
