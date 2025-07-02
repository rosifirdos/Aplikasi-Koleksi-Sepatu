from models.sepatu import Sepatu

class SepatuOlahraga(Sepatu): 
    def __init__(self, merk, model, ukuran, warna, tipe_olahraga, fitur_khusus):
        super().__init__(merk, model, ukuran, warna)
        self.__tipe_olahraga = tipe_olahraga  
        self.__fitur_khusus = fitur_khusus

    def get_tipe_olahraga(self):
        return self.__tipe_olahraga

    def get_fitur_khusus(self):
        return self.__fitur_khusus

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Tipe Olahraga: {self.__tipe_olahraga}, Fitur Khusus: {self.__fitur_khusus}"