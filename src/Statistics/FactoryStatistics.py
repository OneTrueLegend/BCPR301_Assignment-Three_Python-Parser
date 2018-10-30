import plotly
from abc import ABCMeta, abstractmethod

from src.Database import SQLError
from src.Database.SQLiteDatabaseFactory import SQLiteDatabaseFactory
from src.Statistics.ClassData import ClassData


class StatisticsCreator(metaclass=ABCMeta):

    def __init__(self, db_name):
        self.db = SQLiteDatabaseFactory(db_name)

    @abstractmethod
    def create_graph(self):
        pass

    def some_operation(self):
        graph = self.create_graph()
        graph.show_graph()

    def create_tables(self):
        try:
            self.db.query(
                "CREATE TABLE IF NOT EXISTS ClassData (classID INTEGER PRIMARY KEY AUTOINCREMENT, className "
                "TEXT, attributeCount INTEGER, methodCount INTEGER);")
        except SQLError as e:
            print(e)

    def insert_class(self, class_node):
        try:
            self.db.query("INSERT INTO ClassData VALUES(null,'" +
                          class_node.name + "'," +
                          str(len(class_node.attributes)) + "," +
                          str(len(class_node.functions)) + ");")
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


class PlotlyStatisticsCreator(StatisticsCreator):

    def create_graph(self):
        return PlotlyAttributeMethodPerClassGraph()


class Graph(metaclass=ABCMeta):

    @abstractmethod
    def show_graph(self):
        pass


class PlotlyAttributeMethodPerClassGraph(Graph):

    def show_graph(self):
        class_names = []
        class_attributes = []
        class_methods = []
        for class_data in self.get_class_data():
            class_names.append(class_data.class_name)
            class_attributes.append(class_data.attribute_count)
            class_methods.append(class_data.method_count)

        attribute_trace = plotly.graph_objs.Bar(
            x=class_names,
            y=class_attributes,
            name='Attribute Count'
        )

        method_trace = plotly.graph_objs.Bar(
            x=class_names,
            y=class_methods,
            name='Method Count'
        )

        data = [attribute_trace, method_trace]
        layout = plotly.graph_objs.Layout(barmode='group')

        fig = plotly.graph_objs.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='../tmp/grouped-bar.html')
