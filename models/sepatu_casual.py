from models.sepatu import Sepatu

class SepatuCasual(Sepatu): 
    def __init__(self, merk, model, ukuran, warna, material, gaya):
        super().__init__(merk, model, ukuran, warna)
        self.__material = material  
        self.__gaya = gaya

    def get_material(self):
        return self.__material

    def get_gaya(self):
        return self.__gaya

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Material: {self.__material}, Gaya: {self.__gaya}"