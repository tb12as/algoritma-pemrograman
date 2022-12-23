from datetime import datetime
from bangun_datar import persegi
import bangun_datar.segitiga as segitiga

# Tanggal hari ini
today = datetime.today()
print(today.strftime("%d/%m/%Y %H:%M:%S"))

# Tes persegi
print("\nLuas persegi:", persegi.luas(12))
print("Keliling persegi:", persegi.keliling(12))

# Tes segitiga
print("\nLuas segitiga: ", segitiga.luas(12, 13))
print("Keliling segitiga: ", segitiga.keliling(5, 12, 13))
