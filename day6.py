import math
with open('6.txt') as f:
    lines = f.read().splitlines()



time, record =     lines[0].split(': ')[1].split(), lines[1].split(': ')[1].split()
print("d")
timen = ''
recordn = ''

for indv_time,indv_record in zip(time,record):
    timen+=indv_time
    recordn+=indv_record

print(timen,recordn)
timen = int(timen)
recordn = int(recordn)

root1 = (-timen + math.sqrt(timen**2 - (4*recordn)))/-2
root2 = (-timen- math.sqrt(timen**2 - (4*recordn)))/-2

print(-math.ceil(root1)+math.ceil(root2))