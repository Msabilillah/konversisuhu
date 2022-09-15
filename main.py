print("===PROGRAM KONVERSI SUHU SEDERHANA===")

#Celcius
print("...Konversi Suhu Celcius...")
celcius = float(input("Masukkan suhu celcius : "))
suhuFahrenheit = (9 / 5 * celcius) + 32
suhuKelvin = celcius + 273
suhuReamur = (4 / 5 * celcius)
print("Suhu dalam fahrenheit : ", suhuFahrenheit)
print("Suhu dalam kelvin : ", suhuKelvin) 
print("Suhu dalam Reamur :", suhuReamur)

#Fahrenheit
print("...Konversi Suhu Fahrenheit...")
fahrenheit = float(input("Masukkan suhu fahrenheit : "))
suhuCelcius = (fahrenheit -32) * 5 / 9
suhuKelvin = (fahrenheit - 32) * 5 / 9 + 273
suhuReamur = (fahrenheit - 32) * 4 / 9
print("Suhu dalam Celcius :", suhuCelcius)
print("Suhu dalam Kelvin :", suhuKelvin)
print("Suhu dalam Reamur :", suhuReamur)

#Reamur
print("...Konversi Suhu Reamur...")
reamur = float(input("Masukkan suhu reamur : "))
suhuCelcius = (5 / 4 * reamur)
suhuFahrenheit = (9 / 4 * reamur) + 32
suhuKelvin = (5 / 4 * reamur) + 273
print("Suhu dalam Celcius :", suhuCelcius)
print("Suhu dalam Fahrenheit :", suhuFahrenheit)
print("Suhu dalam Kelvin :", suhuKelvin)

#Kelvin
print("...Konversi Suhu Dalam Kelvin...")
kelvin = float(input("Masukkan suhu kelvin : "))
suhuCelcius = kelvin - 273
suhuFahrenheit = (kelvin - 273) * 9 / 5 + 32
suhuReamur = (kelvin - 273) * 4 / 5
print("Suhu dalam Celcius : ", suhuCelcius)
print("Suhu dalam Fahrenheit : ", suhuFahrenheit)
print("Suhu dalam Reamur : ", suhuReamur)