import os
os.system('clear')

nim = [2,3,1,0,3,1,0,3,8,]
print (nim)
# akses item
print ('item indeks 0:',nim[0])
print ('item indeks 0:',nim[3])
print ('item indeks terakhir:',nim[len(nim)-1])
#akses index negatif
print ('item indeks terakhir:',nim[-1])
print ('item indeks terakhir:',nim[-len(nim)])
print ('item index 3:[-6]',nim[-6])
print ('item index 3:[-4]',nim[-4])
print ('item index -7:[2]',nim[2])
print ('item index 2:[-7]',nim[-7])
#akses index batas
print (f'item index 1,2,......: {nim[1:]}')
print (f'item index 3,4,......: {nim[3:]}')
print (f'item index 0,1,2,3:{nim[:4]}')
print (f'item index 0:{nim[:1]}')
print (f'item index semua:{nim[:]}')
print (f'item index [:8]: {nim[:-1]}')
print (f'item index [:4]: {nim[:-5]}')
#pengirisan
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
# nested list
kelas = [('kalkulus1',2),
         ('pemrograman2',3)]
print(kelas)
kelas.append(('pancasila3',2))
kelas.append(('PTI',2))
kelas.append(('Sainster',2))
print(kelas)
# tambahkan matkul 4 dan 5 dan sksnya
print('tugas1')
#mata kuliah 1: matkul1 dengan 2 sks
print (f'mata kuliah 1:{kelas[0][0]}dengan{kelas[1][1]}sks')
#mata kuliah 2: matkul2 dengan 3 sks
print(f'mata kuliah 2:{kelas[1][0]}dengan{kelas[0][1]}sks')
#mata kuliah 3: matkul3 dengan 2 sks
print(f'mata kuliah 3:{kelas[2][0]}dengan{kelas[2][1]}sks')
#mata kuliah 4: matkul4 dengan .. sks
print(f'mata kuliah 4:{kelas[3][0]}dengan{kelas[3][1]}sks')
#mata kuliah 5: matkul5 dengan .. sks
print(f'mata kuliah 5:{kelas[4][0]}dengan{kelas[4][1]}sks')


print()
print("Tugas 2")
data = [('Alwan',2023,'Aktif'),
        (76,98,89,97,99),
        [2,3,2,3,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]

# Nama mahasiswa: Alwan
print(f"Nama mahasiswa : {data[0][0]}")
# Inisial Alwan: A
print(f"Nama mahasiswa : {data[0][0][0]}")
# NIM Alwan: 231031038
nim_int = int("".join(map(str, nim))) 
print(f"NIM {data[0][0]} : {nim_int}")
# Program Alwan: S1-Reguler Sistem Informasi B
print(f"Program {data[0][0]} : {data[3][0]} {data[3][1]}")
# Angkatan Alwan: Ganjil-2023
print(f"Angkatan {data[0][0]}: {data[3][2]}-{data[0][1]}")
# Total sks Alwan adalah: 11
print(f"Total sks {data[0][0]} adalah: {sum(data[2])}")
# Total sks Alwan adalah: 11
print(f"Total sks {data[0][0]} adalah: {sum(data[2])}")
# Jumlah Nilai Alwan: 5
print(f"Jumlah Nilai {data[0][0]}: {len(data[2])}")
# Nilai tertinggi Alwan: 99
print(f"NIlai tertinggi {data[0][0]}: {max(data[1])}")
# Nilai terendah Alwan: 76
print(f"NIlai terendah {data[0][0]}: {min(data[1])}")
# Rata-rata nilai Alwan: 91.8
x_bar = sum(data[1]) / len(data[1])
print(f"Rata-Rata nilai {data[0][0]}: {x_bar}")





