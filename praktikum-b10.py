import os
def judul():
    print('program menghitung volume dan luas permukaan'.center(45))
    print('bangun ruang balok'.center(45))
    print()

def imputan():
    p       = float(input('masukkan panjang :'))
    l       = float(input('masukkan lebar :'))
    t       = float(input('masukkan tinggi :'))
    return p,l,t

def hitung(p,l,t):
    vol = p*l*t
    luas_surf= 2*(p*l*t + p*1)
    luas_non_tuttp = luas_surf -p*1
    return vol,luas_surf,luas_non_tuttp
def tampilan(pesan,nilai):
    print(f'nilai {pesan} : {nilai}')

def pilihan():
    pilih = input('apakah lanjutan [y/n]')
    if pilih == 'y' :
        a= True
    else:
        a= False
        print('Terimah kasih!')
def main():
    os.system('cls')
    judul()                                      #judul 
    p,l,t = imputan()                            #inputan 
    vol,luas_surf,luas_non_tutup = hitung(p,l,t) #hitung
    #tampilan
    tampilan('volume',vol)
    tampilan('luas permukaan',luas_surf)
    tampilan('luas permukaan tanpa tutup',luas_non_tutup)
    a = pilihan()                                #pilihan
    return a
a = True
while a:
    a = main()
