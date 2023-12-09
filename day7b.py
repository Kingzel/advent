
with open('7.txt') as f:
    lines = f.read().splitlines()

hands=[]
imp = ':J23456789TQKA'
lookup =['High Card','One Pair','Two Pair','Three of a kind','Full House','Four of a kind','Five of a kind']
lookupDict ={1:1,2:2,3:4,4:6,5:7}

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


def find_highest_index(d, jCount = 0):

    m = 0
    for key in d:
        if d[key] and key > m:
            m = key

    

    if m==2:
        if len(d[2]) ==2:
            if jCount:
                return 5
            return 3 #Two Pair
    
        else:
            if jCount ==1:
                return 4 # one pair adjustment (1 j -> three of a kind)
            elif jCount >= 2:
                return jCount+4 # one pair adjustment (2 or 3 j -> four and five of a kind)

            return 2 #One Pair
    
    if m==3:
        if d[2]:
            return 5 #Full House
        else:
            if jCount:
                return 5 + jCount

            return 4 #Three of a kind
    if m >=4:
        return m+2+jCount #Four of a kind, Five of a kind (6,7)
    else:
        if m==0:
            return 7
        else:
                return lookupDict[jCount+1]
        


        
    

for i in range(len(lines)):

    hand =lines[i].split()[0]
    bid = int(lines[i].split()[1])
    
    jCount = 0
    handobj= Hand(hand,bid)
    
    temp ={1:[],2:[],3:[],4:[],5:[]}
    seen = []
    for card in hand:
       

        # print(hand)
        if card not in seen and (not(card == 'J')):
            temp[hand.count(card)].append(card)
            seen.append(card)
        
        if card == 'J':
            jCount +=1

    handobj.counts.append(temp)
    handobj.strength =find_highest_index(temp,jCount)
    hands.append(handobj)


hands.sort(key=lambda x: (x.strength,x.val))




rank = 0
acc = 0

for hand in hands:
    rank+=1
    print("Cards: ",hand.cards,"Rank:",rank,"Hand Strength:",(hand.strength,lookup[hand.strength-1]),sep=' | ')
    acc += hand.bid*rank

print("--------------------------")
print("Total winnings:",acc)
