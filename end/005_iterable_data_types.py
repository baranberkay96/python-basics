# Bu örneklerde tuple, list ve dictionary veri tiplerini ve örneklerini inceleyeceğiz

# Tuple veri tipi "immutable" yani değiştirilmezdir.
customers = ('Ahmet', 'Aslı', 'Mehmet')
print(f'cutomers are: {customers}')


# List

customers = ['Ahmet', 'Aslı', 'Mehmet']
print(f'cutomers are: {customers}')

# Listeye eleman ekleme:
customers.append('Ayça')
print(f'cutomers are: {customers}')

# Listeden eleman çıkarma
customers.remove('Aslı')
print(f'cutomers are: {customers}')


# Dictionary'ler bir key'e karşılık bir değerin tutulduğu kullanışlığı veri tipleridir. Süslü parantez ile tanımlanır.

accounts = {
    "Ahmet": ["account 1", "account 2"]
} 

print(f'Ahmetin hesapları: {accounts["Ahmet"]}')

# Ahmete yeni hesap eklemek istersek:

accounts["Ahmet"].append("account 3")
print(f'Ahmetin hesapları: {accounts["Ahmet"]}')

# Yeni bir customer eklemek için:

accounts["Aslı"] = ["account 333"]
print(f'Aslının hesapları: {accounts["Aslı"]}')