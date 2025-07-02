class Sepatu:
    def __init__(self, merk, model, ukuran, warna):
        self.__merk = merk 
        self.__model = model
        self.__ukuran = ukuran
        self.__warna = warna

    def get_merk(self):
        return self.__merk

    def get_model(self):
        return self.__model

    def get_ukuran(self):
        return self.__ukuran

    def get_warna(self):
        return self.__warna

    def display_info(self):
        return f"Merk: {self.__merk}, Model: {self.__model}, Ukuran: {self.__ukuran}, Warna: {self.__warna}"