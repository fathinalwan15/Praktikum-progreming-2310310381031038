pendapatan = int(input('Pendapatan: '))
persentase = 0
bonus = 0
if pendapatan <=1000:
    persentase = 0
elif pendapatan<=2000:
    persentase = 10
elif pendapatan <=3000:
    persentase = 20
elif pendapatan <=4000:
    persentase = 30
elif pendapatan <=5000:
    persentase = 40
else: 
    persentase = 50
bonus =(pendapatann*persentase/100)
total =(pendapatan+bonus)
print('Pendapatan', pendapatan)
print('Persentase', persentase)
print('Bonus', bonus)
print('Total Pendapatan', total)
    

