Import os
os.system('cls')

a= True

while a:
    jawab = input('Apakah ingin melanjutkan (y/n)')
    if jawab == 'y' :
        print('Selamat datang lagi')
        a = True

    if jawab == 'n' :
        print('Sampai ketemu lagi :D')
        a =False

    else:
        os.system ('cls')
        print('Jangan aneh aneh deh :,)')
        a= True