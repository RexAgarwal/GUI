import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
import matplotlib.pyplot as plt
from PySide2.QtGui import QPixmap 
from db import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC

class SKUSelectionBar(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Add the label
        self.label = QLabel("Select SKU", self)
        self.label.setStyleSheet("font-weight: bold; font-size: 16px; margin-right: 10px;")
        layout.addWidget(self.label)

        # Add the dropdown menu
        self.dropdown = QComboBox(self)
        self.dropdown.setStyleSheet("background-color: #f0f0f0; border: 1px solid #d9d9d9; padding: 5px;")
        self.dropdown.addItem("SKU1")
        self.dropdown.addItem("SKU2")
        layout.addWidget(self.dropdown)

        # Set maximum height and width
        self.setMaximumHeight(50)
        self.setMaximumWidth(200)




class ImageGalleryTab(QWidget):
    unit_type = "all"

    def __init__(self):
        super().__init__()

        # Create a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a content widget to hold the image grid
        content_widget = QWidget(scroll_area)

        # Create a filter layout with three buttons
        filter_layout = QHBoxLayout()
        filter_layout.setContentsMargins(20, 20, 20, 20)

        all_button = QPushButton("All", self)
        good_button = QPushButton("Good", self)
        bad_button = QPushButton("Bad", self)

        filter_layout.addWidget(all_button)
        filter_layout.addWidget(good_button)
        filter_layout.addWidget(bad_button)

        all_button.clicked.connect(lambda: self.show_units("all",scroll_area))
        good_button.clicked.connect(lambda: self.show_units("Good",scroll_area))
        bad_button.clicked.connect(lambda: self.show_units("Bad",scroll_area))

        # Create a grid layout with 3 rows and 6 columns
        grid_layout = QGridLayout(content_widget)
        grid_layout.setSpacing(20)

        # Add the filter layout to the content widget
        grid_layout.addLayout(filter_layout, 0, 0, 1, 6)

        results = units_collection.find({})
        i = 0

        # print(va)
        # Add images to the grid
        for result in results:
            # Create a frame to hold the image
            frame = QFrame(self)
            frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
            frame.setFixedSize(100, 120)

            # Load the image into a QLabel
            label = QLabel(self)
            pixmap = QPixmap('Images/{}.jpg'.format(result["unit_id"]))
            label.setPixmap(pixmap.scaledToWidth(100))

            # Add the label to the frame
            layout = QHBoxLayout(frame)
            layout.addWidget(label)
            layout.setAlignment(Qt.AlignCenter)

            # Create a line widget for the status
            line = QFrame(self)
            line.setFixedHeight(5)
            line.setStyleSheet("background-color: {};".
                               format("green" if result["status"] == "Good" else "red"))

            # Add the line to the label
            label_layout = QVBoxLayout(label)
            label_layout.addWidget(line, 1, Qt.AlignBottom)

            # Add the frame to the grid
            row = i // 6
            col = i % 6
            grid_layout.addWidget(frame, row+1, col)
            i += 1

        # Add the grid layout to the content widget
        content_widget.setLayout(grid_layout)

        # Set the content widget to the scroll area
        scroll_area.setWidget(content_widget)

        # Add the scroll area to the layout
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)
        self.setLayout(layout)


    def show_units(self,unit_type,scroll_area):


        # Remove any existing parent from scroll_area
        self.layout().removeWidget(scroll_area)
             
        # Create a content widget to hold the image grid
        content_widget = QWidget(scroll_area)

        self.unit_type = unit_type

        # Create a filter layout with three buttons
        filter_layout = QHBoxLayout()
        filter_layout.setContentsMargins(20, 20, 20, 20)

        all_button = QPushButton("All", self)
        good_button = QPushButton("Good", self)
        bad_button = QPushButton("Bad", self)

        filter_layout.addWidget(all_button)
        filter_layout.addWidget(good_button)
        filter_layout.addWidget(bad_button)

        all_button.clicked.connect(lambda: self.show_units("all",scroll_area))
        good_button.clicked.connect(lambda: self.show_units("Good",scroll_area))
        bad_button.clicked.connect(lambda: self.show_units("Bad",scroll_area))

        # Create a grid layout with 3 rows and 6 columns
        grid_layout = QGridLayout(content_widget)
        grid_layout.setSpacing(20)

        # Add the filter layout to the content widget
        grid_layout.addLayout(filter_layout, 0, 0, 1, 6)

        if self.unit_type != "all":
            results = units_collection.find({"status":self.unit_type})
        else: 
            results = units_collection.find({})

        i = 0
        # Add images to the grid
        for result in results:
            # Create a frame to hold the image
            frame = QFrame(self)
            frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
            frame.setFixedSize(100, 120)

            # Load the image into a QLabel
            label = QLabel(self)
            pixmap = QPixmap('Images/{}.jpg'.format(result["unit_id"]))
            label.setPixmap(pixmap.scaledToWidth(100))

            # Add the label to the frame
            layout = QHBoxLayout(frame)
            layout.addWidget(label)
            layout.setAlignment(Qt.AlignCenter)

            # Create a line widget for the status
            line = QFrame(self)
            line.setFixedHeight(5)
            line.setStyleSheet("background-color: {};".
                               format("green" if result["status"] == "Good" else "red"))

            # Add the line to the label
            label_layout = QVBoxLayout(label)
            label_layout.addWidget(line, 1, Qt.AlignBottom)

            # Add the frame to the grid
            row = i // 6
            col = i % 6
            grid_layout.addWidget(frame, row+1, col)
            i += 1

        # Add the grid layout to the content widget
        content_widget.setLayout(grid_layout)

        # Set the content widget to the scroll area
        scroll_area.setWidget(content_widget)

        # Add the scroll area to the layout
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
        print(unit_type)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window")
        self.setGeometry(100, 100, 1000, 500)

        # Create a tab widget
        tab_widget = QTabWidget(self)

        # Create the first tab
        analytics_tab = QWidget()
        analytics_layout = QVBoxLayout()
        

        # Create the SKU selection bar
        sku_selection_bar = SKUSelectionBar()
        analytics_layout.addWidget(sku_selection_bar)

            # Create the matplotlib figure
        fig, ax = plt.subplots(figsize=(6,3), dpi=100)

            # Add the bar chart data
        x = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM']
        good = [60, 60, 90, 90, 90]
        bad = [10, 10, 10, 10, 10]
        ax.bar(x, good, color='orange', label='Good',width=0.4)
        ax.bar(x, bad, color='green', label='Bad', bottom=good,width=0.4)

            # Set the axis labels and legend
        ax.set_ylabel('Percentage')
        ax.set_xlabel('Time')
        legend = ax.legend(bbox_to_anchor=(1, 1), loc='upper left')
        legend.get_frame().set_facecolor('white')

            # Add the matplotlib figure to the layout
        canvas = FC(fig)
        analytics_layout.addWidget(canvas)

        analytics_tab.setLayout(analytics_layout)
        tab_widget.addTab(analytics_tab, "Analytics")

        # create second tab


        image_gallery_tab = ImageGalleryTab()
        tab_widget.addTab(image_gallery_tab, "Image gallery")

        # Add the tab widget to the main window
        self.setCentralWidget(tab_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # create_data()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
