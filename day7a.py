
with open('7.txt') as f:
    lines = f.read().splitlines()

hands=[]
imp = ':23456789TJQKA'


class Hand:
    def __init__(self,string,bid) -> None:
        self.cards = string
        self.bid = bid
        self.strength = 0
        self.counts =[]
        self.val = self.valuefind()
        
    
    def valuefind(self):
        torr = ''
        for j in range(5):
            torr += str(hex(imp.index(self.cards[j])))[2]
        return int(torr,16)


def find_highest_index(d):
    m = 1
    for key in d:
        if d[key] and key > m:
            m = key
    if m==2:
        if len(d[2]) ==2:
            return 3
        else:
            return 2
    
    if m==3:
        if d[2]:
            return 5
        else:
            return 4
    if m >=4:
        return m+2
    else:
        return m
  
        
    

for i in range(len(lines)):

    hand =lines[i].split()[0]
    bid = int(lines[i].split()[1])
    
    
    handobj= Hand(hand,bid)
    
    temp ={1:[],2:[],3:[],4:[],5:[]}
    seen = []
    for card in hand:
       

        # print(hand)
        if card not in seen:
            temp[hand.count(card)].append(card)
            seen.append(card)

    handobj.counts.append(temp)
    handobj.strength =find_highest_index(temp)
    hands.append(handobj)



hands.sort(key=lambda x: (x.strength,x.val))




count = 0
acc = 0

for hand in hands:
    count+=1
    # print("Cards: ",hand.cards,"Rank:",count,"Hand Strength:",hand.strength,sep=' | ')
    acc += hand.bid*count

print("--------------------------")
print("Total winnings:",acc)
