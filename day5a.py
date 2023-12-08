seed_to_soil=[]
soil_to_fertilizer=[]
fertilizer_to_water=[]
water_to_light=[]
light_to_temp=[]
temp_to_humid=[]
humid_to_loc =[]
seeds = {}

ss=sf=fw=wl=lt=th=hl=0

with open('5.txt') as f:
    lines = f.read().splitlines()

seeds = {int(seed):-1 for seed in lines[0].split(':')[1].split()}
# print(seeds)
for i in range(1,len(lines)):
        if lines[i]:            
            # print(lines[i])
            if 'seed-to-soil' in lines[i].split(':')[0]:
                 ss = i
            if 'soil-to-fert' in lines[i].split(':')[0]:
                 sf =i
            if 'fertilizer-to-water' in lines[i].split(':')[0]:
                 fw = i
            if 'water-to-light' in lines[i].split(':')[0]:
                 wl = i
            if 'light-to-temp' in lines[i].split(':')[0]:
                 lt = i
            if 'temperature-to-humidity' in lines[i].split(':')[0]:
                 th = i
            if 'humidity-to-location' in lines[i].split(':')[0]:
                 hl = i

# print(ss,sf,fw,wl,lt,th,hl)

     



seed_to_soil = [[int(x.split()[1]),int(x.split()[1])+int(x.split()[2]),int(x.split()[0]),int(x.split()[0])+int(x.split()[2])] for x in lines[ss+1:sf-1]]
soil_to_fertilizer = [[int(x.split()[1]),int(x.split()[1])+int(x.split()[2]),int(x.split()[0]),int(x.split()[0])+int(x.split()[2])] for x in lines[sf+1:fw-1] ]
fertilizer_to_water = [[int(x.split()[1]),int(x.split()[1])+int(x.split()[2]),int(x.split()[0]),int(x.split()[0])+int(x.split()[2])] for x in lines[fw+1:wl-1]]
water_to_light = [[int(x.split()[1]),int(x.split()[1])+int(x.split()[2]),int(x.split()[0]),int(x.split()[0])+int(x.split()[2])] for x in lines[wl+1:lt-1] ]
light_to_temp = [[int(x.split()[1]),int(x.split()[1])+int(x.split()[2]),int(x.split()[0]),int(x.split()[0])+int(x.split()[2])] for x in lines[lt+1:th-1] ]
temp_to_humid = [[int(x.split()[1]),int(x.split()[1])+int(x.split()[2]),int(x.split()[0]),int(x.split()[0])+int(x.split()[2])] for x in lines[th+1:hl-1] ]
humid_to_loc =[[int(x.split()[1]),int(x.split()[1])+int(x.split()[2]),int(x.split()[0]),int(x.split()[0])+int(x.split()[2])] for x in lines[hl+1:] ] 

# print(seed_to_soil,soil_to_fertilizer,fertilizer_to_water,water_to_light,light_to_temp,temp_to_humid,humid_to_loc,sep="\n")

for seed in seeds:
     for Range in seed_to_soil:
          if seed in range(Range[0],Range[1]):
               seeds[seed]=Range[2]+seed-Range[0]
               break
     
     if seeds[seed] == -1:
        seeds[seed]=seed
        
     for Range in soil_to_fertilizer:
          if seeds[seed] in range(Range[0],Range[1]):
               seeds[seed]=Range[2]+seeds[seed]-Range[0]
               break
    
     for Range in fertilizer_to_water:
          if seeds[seed] in range(Range[0],Range[1]):
               seeds[seed]=Range[2]+seeds[seed]-Range[0]
               break
     
     for Range in water_to_light:
          if seeds[seed] in range(Range[0],Range[1]):
               seeds[seed]=Range[2]+seeds[seed]-Range[0]
               break

     for Range in light_to_temp:
          if seeds[seed] in range(Range[0],Range[1]):
               seeds[seed]=Range[2]+seeds[seed]-Range[0]
               break
    
     for Range in temp_to_humid:
          if seeds[seed] in range(Range[0],Range[1]):
               seeds[seed]=Range[2]+seeds[seed]-Range[0]
               break
              
     for Range in humid_to_loc:
          if seeds[seed] in range(Range[0],Range[1]):
               seeds[seed]=Range[2]+seeds[seed]-Range[0]
               break
     
          
print(min(seeds.values()))
