import ast

from algorithm import prim
from algorithm import kruskal
from utils import utils
from algorithm import cluster
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

# G = nx.DiGraph()
#
# arr = [
#     [0, 4, 0, 0, 0, 10, 7],
#     [4, 0, 1, 3, 0, 0, 0],
#     [0, 1, 0, 2, 0, 0, 0],
#     [0, 3, 2, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0, 2, 5],
#     [10, 0, 0, 0, 2, 0, 3],
#     [7, 0, 0, 1, 5, 3, 0]
# ]
#
# p, w = prim.prim(arr,5)
# test = [i for i in range(len(p))]
# G.add_nodes_from(test)
#
# for i in range(len(p)):
#     if p[i] != -1:
#         G.add_weighted_edges_from([(i, p[i], w[i])])
#
# pos = nx.kamada_kawai_layout(G, weight='weight')
# nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', edge_color='gray')
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# # nx.draw_networkx(G, pos)
# plt.show()


# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i][j] != 0:
#             G.add_weighted_edges_from([(i, j, arr[i][j])])
#
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', edge_color='gray')
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
#
# plt.show()
# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random


# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.matrix = []

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.choose_file_button = QPushButton('Choose File')
        self.choose_file_button.clicked.connect(self.choose_file)

        self.graph_button = QPushButton('Show Graph')
        self.graph_button.clicked.connect(self.graph_ori)
        self.mst_prim_button = QPushButton('Show MST Prim')
        self.mst_prim_button.clicked.connect(self.mst_prim)
        self.mst_kruskal_button = QPushButton('Show MST Kruskal')
        self.mst_kruskal_button.clicked.connect(self.mst_kruskal)

        self.delete_node_textfield = QLineEdit()
        self.number_node_delete = 0
        self.delete_node_button = QPushButton("delete")
        self.delete_node_button.clicked.connect(self.delete_node)
        delete_layout = QVBoxLayout()
        delete_tb_layout = QHBoxLayout()
        delete_tb_layout.addWidget(self.delete_node_textfield)
        delete_tb_layout.addWidget(self.delete_node_button)
        delete_label = QLabel("delete node")
        delete_layout.addWidget(delete_label)
        delete_layout.addLayout(delete_tb_layout)

        self.add_node_textfield = QLineEdit()
        self.add_node_button = QPushButton("add")
        self.add_node_button.clicked.connect(self.add_node)
        self.add_arr = ""
        add_layout = QVBoxLayout()
        add_tb_layout = QHBoxLayout()
        add_tb_layout.addWidget(self.add_node_textfield)
        add_tb_layout.addWidget(self.add_node_button)
        add_label = QLabel("add node")
        add_layout.addWidget(add_label)
        add_layout.addLayout(add_tb_layout)

        self.cluster_textfield = QLineEdit()
        self.cluster_button = QPushButton("cluster")
        self.cluster_button.clicked.connect(self.cluster)
        self.number_cluster = 0
        cluster_layout = QVBoxLayout()
        cluster_tb_layout = QHBoxLayout()
        cluster_tb_layout.addWidget(self.cluster_textfield)
        cluster_tb_layout.addWidget(self.cluster_button)
        cluster_label = QLabel("cluster")
        cluster_layout.addWidget(cluster_label)
        cluster_layout.addLayout(cluster_tb_layout)


        layout_button = QHBoxLayout()

        layout_button.addWidget(self.graph_button)
        layout_button.addWidget(self.mst_prim_button)
        layout_button.addWidget(self.mst_kruskal_button)


        layout_manip_data = QVBoxLayout()
        layout_manip_data.addLayout(delete_layout)
        layout_manip_data.addLayout(add_layout)
        layout_manip_data.addLayout(cluster_layout)


        layout_menu = QHBoxLayout()
        layout_menu.addLayout(layout_manip_data)
        layout_menu.addWidget(self.choose_file_button)

        layout_main = QVBoxLayout()

        layout_main.addWidget(self.toolbar)
        layout_main.addLayout(layout_button)
        layout_main.addWidget(self.canvas)
        layout_main.addLayout(layout_menu)

        self.delete_node_textfield.textChanged.connect(self.on_input_delete_changed)
        self.delete_node_textfield.setPlaceholderText("0")
        self.add_node_textfield.textChanged.connect(self.on_input_add_changed)
        self.add_node_textfield.setPlaceholderText("[0,0,0,0,0,....]")
        self.cluster_textfield.textChanged.connect(self.on_input_cluster_changed)
        self.cluster_textfield.setPlaceholderText("0")
        self.setLayout(layout_main)

    def on_input_delete_changed(self, text):
        if text == '':
            self.number_node_delete = 0
            return
        try:
            self.number_node_delete = int(text)
        except ValueError:
            self.number_node_delete = 0

    def on_input_add_changed(self, text):
        self.add_arr = text

    def on_input_cluster_changed(self, text):
        if text == '':
            self.number_cluster = 0
            return
        try:
            self.number_cluster = int(text)
        except ValueError:
            self.number_cluster = 0
        print(self.number_cluster)

    def delete_node(self):
        if len(self.matrix) == 0:
            return

        self.figure.clear()
        G = nx.Graph()

        test = [i for i in range(len(self.matrix))]
        G.add_nodes_from(test)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != 0:
                    G.add_weighted_edges_from([(i, j, self.matrix[i][j])])

        print(self.number_node_delete)
        G.remove_node(self.number_node_delete)

        pos = nx.spring_layout(G, weight='weight')
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold',
                edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        self.matrix = nx.to_numpy_array(G)

        self.canvas.draw_idle()

    def add_node(self):
        self.figure.clear()

        if len(self.matrix) == 0:
            return
        G = nx.Graph()

        test = [i for i in range(len(self.matrix))]
        G.add_nodes_from(test)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != 0:
                    G.add_weighted_edges_from([(i, j, self.matrix[i][j])])

        if self.add_arr == "":
            return


        try:
            more_node = ast.literal_eval(self.add_arr)
        except ValueError:
            return

        for i in range(len(more_node)):
            if more_node[i] != 0:
                G.add_weighted_edges_from([(i, len(self.matrix), more_node[i])])

        pos = nx.spring_layout(G, weight='weight')
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold',
                edge_color='gray')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        self.matrix = nx.to_numpy_array(G)

        self.canvas.draw_idle()

    def cluster(self):
        self.figure.clear()

        if len(self.matrix) == 0:
            return

        if self.number_cluster == 0:
            return

        if self.number_cluster > len(self.matrix) or self.number_cluster < 1:
            return

        G = nx.Graph()
        cluster_res = cluster.cluster(self.matrix,self.number_cluster)
        print(cluster_res)
        print(len(cluster_res[0]))
        test = [i for i in range(len(cluster_res[0]))]
        G.add_nodes_from(test)



        edge_colors = [f'#%06x' % random.randint(0, 0xFFFFFF) for _ in range(len(cluster_res))]
        edge_colors_nx = {}

        for i in range(len(cluster_res)):
            for j in range(len(cluster_res[0])):
                for k in range(len(cluster_res[0])):
                    if cluster_res[i][j][k] != 0:
                        G.add_weighted_edges_from([(j, k, cluster_res[i][j][k])])
                        edge_colors_nx[(j,k)] = edge_colors[i]

        edges = G.edges()
        colors = [edge_colors_nx[edge] for edge in edges]
        pos = nx.spring_layout(G, weight='weight')
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', edge_color=colors,
                width=3.0)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        self.canvas.draw_idle()







    def mst_prim(self):

        self.figure.clear()

        if len(self.matrix) == 0:
            return
        G = nx.DiGraph()

        p, w = prim.prim(self.matrix)
        test = [i for i in range(len(p))]
        G.add_nodes_from(test)

        for i in range(len(p)):
            if p[i] != -1:
                G.add_weighted_edges_from([(i, p[i], w[i])])

        pos = nx.spring_layout(G, weight='weight')
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', edge_color='gray', width = 3.0)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        self.canvas.draw_idle()

    def mst_kruskal(self):

        self.figure.clear()

        if len(self.matrix) == 0:
            return
        G = nx.DiGraph()

        p, w = kruskal.kruskal(self.matrix)
        test = [i for i in range(len(p))]
        G.add_nodes_from(test)

        for i in range(len(p)):
            if p[i] != -1:
                G.add_weighted_edges_from([(i, p[i], w[i])])

        pos = nx.spring_layout(G, weight='weight')
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', edge_color='gray', width = 3.0)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        self.canvas.draw_idle()

    def graph_ori(self):
        self.figure.clear()

        if len(self.matrix) == 0:
            return
        G = nx.Graph()


        test = [i for i in range(len(self.matrix))]
        G.add_nodes_from(test)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != 0:
                    G.add_weighted_edges_from([(i, j, self.matrix[i][j])])

        pos = nx.spring_layout(G, weight='weight')
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_weight='bold', edge_color=f'#%06x' % random.randint(0, 0xFFFFFF))
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        print(nx.to_numpy_array(G)[0][0])

        self.canvas.draw_idle()

    def choose_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)", options=options)

        if file_name:
            with open(file_name, 'r') as file:
                contents = file.read()

                try:
                    data_array = ast.literal_eval(contents)
                except SyntaxError:
                    print("Error: Invalid data format in the file.")
                    return

                if not isinstance(data_array, list) or not all(isinstance(row, list) for row in data_array):
                    print("Error: The data in the file is not a valid matrix.")
                    return

                self.matrix = data_array



# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())


