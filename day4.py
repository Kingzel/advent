with open("4.txt") as f:
    lines = f.read().splitlines()

acc =0
for card in lines:
   count = 0
   card_stats = card.split(':',-1)[1]
   winners_raw,ours_raw = card_stats.split('|')
   winners = winners_raw.split()
   ours = ours_raw.split()
   for winning_num in winners:
       if winning_num in ours:
           count+=1
   if count ==0:
       acc +=0
   else:
    acc += 2**(count-1)


print(acc)