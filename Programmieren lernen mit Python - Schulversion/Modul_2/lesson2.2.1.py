from daten import sitze, ort

if sitze == 4 and (ort == "Fenster" or ort == "Tür"):
    print("Juhu, den Tisch nehmen wir.")
elif sitze != 4:
    print("Wir brauchen einen Tisch mit genau 4 Sitzen.")
else:
    print("Der Tisch hat zwar die richtige Größe, ist aber weder am Fenster noch an der Tür.")
