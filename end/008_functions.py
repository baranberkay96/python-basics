# Bu konuda fonksiyon örneklemeleri yapacağız.


def bakiye_hesaplama(bakiye, tutar):
    if tutar > bakiye:
        return "Bakiyeniz yeterli değil."
    else:
        return bakiye - tutar

bakiye = 1000

tutar = 200

kalan = bakiye_hesaplama(1000, 200)
print("Kalan bakiye: ", kalan)