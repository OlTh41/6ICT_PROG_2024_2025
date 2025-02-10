import cv2
from matplotlib import pyplot as plt

def plt_imshow(titel, afbeelding):
    plt.imshow(afbeelding, cmap='Greys_r')
    plt.title(titel)
    plt.grid(False)
    plt.show()

## Afbeelding inladen (met grijswaarden).
driehoek = cv2.imread(r"_afbeeldingen/driehoek.jpg")
driehoek_grijs = cv2.cvtColor(driehoek, cv2.COLOR_BGR2GRAY)

# Drempel gebruiken om driehoek & achtergrond volledig te scheiden.
# Alle pixels kleiner dan 127 worden 0, groter dan 127 worden 255.
_, driehoek_drempel = cv2.threshold(driehoek_grijs, 127, 255, cv2.THRESH_BINARY)

# Afbeelding & pixelwaarden tonen.
plt_imshow("grijsafbeelding met drempel", driehoek_drempel)
print(driehoek_drempel)

# Afbeelding & pixelwaarden tonen.
plt_imshow("grijsafbeelding", driehoek_grijs)
print(driehoek_grijs)# Afbeelding inladen.
