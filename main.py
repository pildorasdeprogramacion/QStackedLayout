
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QLineEdit, QTextEdit, QPushButton,
    QStackedLayout, QFormLayout, QVBoxLayout, QHBoxLayout, QComboBox, QDateEdit,
    QMessageBox)
from PyQt6.QtCore import Qt,QDate
from PyQt6.QtGui import QPixmap, QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(500, 580)
        self.setWindowTitle("QStackedLayout")
        self.generate_window()
        self.show()

    def generate_window(self):
        botton_1 = QPushButton("Ventana 1")
        botton_1.clicked.connect(self.change_window)
        botton_2 = QPushButton("Ventana 2")
        botton_2.clicked.connect(self.change_window)
        botton_3 = QPushButton("Ventana 3")
        botton_3.clicked.connect(self.change_window)

        buttons_group = QHBoxLayout()
        buttons_group.addWidget(botton_1)
        buttons_group.addWidget(botton_2)
        buttons_group.addWidget(botton_3)

        #Pagina 1
        tittle = QLabel("Mapa")
        tittle.setFont(QFont("Arial",18))
        tittle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Obtener el tamaño de la ventana
        window_size = self.size()

        image_map = QLabel()
        pixmap = QPixmap("images/map.png")
        image_map.setPixmap(pixmap)
        image_map.setMaximumSize(window_size)
        image_map.setScaledContents(True)

        page1_layout = QVBoxLayout()
        page1_layout.addWidget(tittle)
        page1_layout.addWidget(image_map)

        container_1 = QWidget()
        container_1.setLayout(page1_layout)


        #Pagina 2
        title2 = QLabel("Solicitud de ingreso")
        title2.setFont(QFont("Arial",18))
        title2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Nombre")
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Apellido")

        self.genero_selection = QComboBox()
        self.genero_selection.addItems(["Masculino", "Femenino"])
        self.fecha_nacimiento_edit = QDateEdit()
        self.fecha_nacimiento_edit.setDisplayFormat("yyyy-MM-dd")
        self.fecha_nacimiento_edit.setMaximumDate(
            QDate.currentDate())
        self.fecha_nacimiento_edit.setCalendarPopup(True)
        self.fecha_nacimiento_edit.setDate(QDate.currentDate())

        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("601-545454")

        submit_button = QPushButton("SUBMIT")
        submit_button.clicked.connect(self.mostrar_info)

        primer_h_box = QHBoxLayout()
        primer_h_box.addWidget(self.nombre_edit)
        primer_h_box.addWidget(self.apellido_edit)

        form_2 = QFormLayout()
        form_2.addRow(title2)
        form_2.addRow("Nombre: ",primer_h_box)
        form_2.addRow("Genero: ",self.genero_selection)
        form_2.addRow("fecha: ",self.fecha_nacimiento_edit)
        form_2.addRow("Telefono: ",self.telefono)
        form_2.addRow(submit_button)

        #self.setLayout(form_2)
        container_2 = QWidget()
        container_2.setLayout(form_2)


        #Pagina 3
        title3 = QLabel("Observaciones")
        title3.setFont(QFont("Arial",18))
        title3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.observations = QTextEdit()
        form_3 = QFormLayout()
        form_3.addRow(title3)
        form_3.addRow("Observaciones", self.observations)

        #self.setLayout(form_2)
        container_3 = QWidget()
        container_3.setLayout(form_3)


        #Creamos el stacked

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_1)
        self.stacked_layout.addWidget(container_2)
        self.stacked_layout.addWidget(container_3)

        # creamos el Layout

        main_layout = QVBoxLayout()
        main_layout.addLayout(buttons_group)
        main_layout.addLayout(self.stacked_layout)
        self.setLayout(main_layout)

    
    def change_window(self):
        button = self.sender()
        if button.text().lower() == 'ventana 1':
            self.stacked_layout.setCurrentIndex(0)
        elif button.text().lower() == 'ventana 2':
            self.stacked_layout.setCurrentIndex(1)
        else:
            self.stacked_layout.setCurrentIndex(2)



    
    def mostrar_info(self):
        QMessageBox.information(self, 
                                "Informacion",
                                f"Nombre: {self.nombre_edit.text()} {self.nombre_edit.text()}\n \
                                  Genero: {self.genero_selection.currentText()}\n \
                                  fecha: {self.fecha_nacimiento_edit.text()} \n \
                                  telefono: {self.telefono.text()}",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
