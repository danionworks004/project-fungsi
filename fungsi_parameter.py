def selamat_datang(nama):
    print('halo',nama,'apa kabar?')
    
selamat_datang('budi')

print('='*50)

def greetings(nama,waktu):
    print('halo',nama,'selamat',waktu)
    
greetings('andi','pagi') #positional parameter

greetings(waktu='malam',nama='wahyu') #named parameter

def penjumlahan(a,b):
    hasil = a+b
    return hasil

data_greeting = greetings('wahyu','pagi')
hasil_jumlah = penjumlahan(2, 5)
print(data_greeting)
print(hasil_jumlah)