import plotly

from src.Statistics.AbstractGraph import AbstractGraph


class BarMethodGraph(AbstractGraph):
    def initialize(self):
        self.class_names = []
        self.class_methods = []

    def insert(self, class_data_list):
        for class_data in class_data_list:
            self.class_names.append(class_data.class_name)
            self.class_methods.append(class_data.method_count)

        self.method_trace = plotly.graph_objs.Bar(
            x=self.class_names,
            y=self.class_methods,
            name='Method Count'
        )

    def finalize(self):
        data = [self.method_trace]
        layout = plotly.graph_objs.Layout(barmode='group')

        fig = plotly.graph_objs.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='../tmp/grouped-bar.html')
