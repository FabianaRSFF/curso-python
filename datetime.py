from  datetime import datetime, timedelta


data = datetime(2021, 10, 24, 9, 45, 50)
print(data)
#Formatando a data para o fuso brasileiro:

print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('24/10/2021', '%d/%m/%Y')
print(data.timestamp())


data = datetime.fromtimestamp(1635044400.0)
print(data)


data = datetime.strptime('24/10/2021 20:00:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(seconds=2*60*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('24/10/2021 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('22/10/2020 16:00:00', '%d/%m/%Y %H:%M:%S')
dif = d1 - d2
print(dif)