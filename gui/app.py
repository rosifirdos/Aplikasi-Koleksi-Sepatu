from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QMessageBox, QFormLayout
)
from PyQt5.QtCore import Qt

from models.sepatu import Sepatu
from models.sepatu_olahraga import SepatuOlahraga
from models.sepatu_casual import SepatuCasual

class ShoeCollectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manajemen Koleksi Sepatu (PyQt5)")
        self.setGeometry(100, 100, 600, 400) 

        self.shoe_collection = [] 
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.merk_input = QLineEdit(self)
        form_layout.addRow("Merk:", self.merk_input)

        self.model_input = QLineEdit(self)
        form_layout.addRow("Model:", self.model_input)

        self.ukuran_input = QLineEdit(self)
        form_layout.addRow("Ukuran:", self.ukuran_input)

        self.warna_input = QLineEdit(self)
        form_layout.addRow("Warna:", self.warna_input)

        self.shoe_type_combo = QComboBox(self)
        self.shoe_type_combo.addItem("Pilih Tipe")
        self.shoe_type_combo.addItem("Sepatu Olahraga")
        self.shoe_type_combo.addItem("Sepatu Casual")
        self.shoe_type_combo.addItem("Sepatu Biasa")
        form_layout.addRow("Tipe Sepatu:", self.shoe_type_combo)
        self.shoe_type_combo.currentIndexChanged.connect(self.on_shoe_type_selected) 

        self.specific_label1 = QLabel("")
        self.specific_input1 = QLineEdit(self)
        self.specific_label2 = QLabel("")
        self.specific_input2 = QLineEdit(self)

        self.specific_row1_widget = QWidget()
        self.specific_row1_layout = QHBoxLayout(self.specific_row1_widget)
        self.specific_row1_layout.addWidget(self.specific_label1)
        self.specific_row1_layout.addWidget(self.specific_input1)
        self.specific_row1_layout.setContentsMargins(0, 0, 0, 0) 

        self.specific_row2_widget = QWidget()
        self.specific_row2_layout = QHBoxLayout(self.specific_row2_widget)
        self.specific_row2_layout.addWidget(self.specific_label2)
        self.specific_row2_layout.addWidget(self.specific_input2)
        self.specific_row2_layout.setContentsMargins(0, 0, 0, 0) 

        form_layout.addRow(self.specific_row1_widget)
        form_layout.addRow(self.specific_row2_widget)

        self.hide_specific_fields() 

        main_layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Tambah Sepatu", self)
        self.add_button.clicked.connect(self.add_shoe) 
        button_layout.addWidget(self.add_button)

        self.display_button = QPushButton("Tampilkan Koleksi", self)
        self.display_button.clicked.connect(self.display_collection) 
        button_layout.addWidget(self.display_button)
        main_layout.addLayout(button_layout)

        self.collection_text = QTextEdit(self)
        self.collection_text.setReadOnly(True)
        main_layout.addWidget(self.collection_text)

        self.setLayout(main_layout)

    def hide_specific_fields(self):
        self.specific_row1_widget.hide()
        self.specific_row2_widget.hide()
        self.specific_input1.clear()
        self.specific_input2.clear()

    def show_specific_fields(self, label1_text, label2_text):
        self.specific_label1.setText(label1_text)
        self.specific_label2.setText(label2_text)
        self.specific_row1_widget.show()
        self.specific_row2_widget.show()

    def on_shoe_type_selected(self, index):
        selected_type = self.shoe_type_combo.currentText()
        self.hide_specific_fields()

        if selected_type == "Sepatu Olahraga":
            self.show_specific_fields("Tipe Olahraga:", "Fitur Khusus:")
        elif selected_type == "Sepatu Casual":
            self.show_specific_fields("Material:", "Gaya:")

    def add_shoe(self):
        merk = self.merk_input.text()
        model = self.model_input.text()
        ukuran_str = self.ukuran_input.text()
        warna = self.warna_input.text()
        shoe_type = self.shoe_type_combo.currentText()

        if not all([merk, model, ukuran_str, warna, shoe_type != "Pilih Tipe"]):
            QMessageBox.critical(self, "Error", "Semua field harus diisi!")
            return

        try:
            ukuran = float(ukuran_str)
        except ValueError:
            QMessageBox.critical(self, "Error", "Ukuran harus angka!")
            return

        shoe = None
        if shoe_type == "Sepatu Olahraga":
            tipe_olahraga = self.specific_input1.text()
            fitur_khusus = self.specific_input2.text()
            if not all([tipe_olahraga, fitur_khusus]):
                QMessageBox.critical(self, "Error", "Field khusus sepatu olahraga harus diisi!")
                return
            shoe = SepatuOlahraga(merk, model, ukuran, warna, tipe_olahraga, fitur_khusus)
        elif shoe_type == "Sepatu Casual":
            material = self.specific_input1.text()
            gaya = self.specific_input2.text()
            if not all([material, gaya]):
                QMessageBox.critical(self, "Error", "Field khusus sepatu casual harus diisi!")
                return
            shoe = SepatuCasual(merk, model, ukuran, warna, material, gaya)
        elif shoe_type == "Sepatu Biasa":
            shoe = Sepatu(merk, model, ukuran, warna)

        if shoe:
            self.shoe_collection.append(shoe)
            QMessageBox.information(self, "Sukses", "Sepatu berhasil ditambahkan!")
            self.clear_entries()
            self.display_collection()

    def display_collection(self):
        self.collection_text.clear()
        if not self.shoe_collection:
            self.collection_text.setText("Koleksi sepatu kosong.")
            return

        for i, shoe in enumerate(self.shoe_collection):
            self.collection_text.append(f"{i+1}. {shoe.display_info()}")

    def clear_entries(self):
        self.merk_input.clear()
        self.model_input.clear()
        self.ukuran_input.clear()
        self.warna_input.clear()
        self.shoe_type_combo.setCurrentIndex(0) 
        self.hide_specific_fields()