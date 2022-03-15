#Python Physik Input (Temperatur, Luftdruck, Wind, Luftfeuchtigkeit, Niederschlag)

print("Wovon brauchst du die Infos?")
a = input("Temperatur, Luftdruck, Wind, Luftfeuchtigkeit, Niederschlag:   ")

if a in ['Temperatur']:
    print("Einheit: Grad Celsius   Messgerät: Thermometer")

if a in ['Luftdruck']:
    print("Einheit: bar, hPa, psi   Messgerät: Barometer")

if a in ['Wind']:
    print("Einheit: km/h   Messgerät: Anemometer")

if a in ['Luftfeuchtigkeit']:
    print("Einheit: absolute Feuchte: g/m³, Relative Feuchte: %   Messgerät: Hygrometer")

if a in ['Niederschlag']:
    print("Einheit: ml Messgerät: Regenmesser, Hyetometer")
