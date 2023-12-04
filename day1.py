word_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
with open("lines.txt") as f:
    lines = f.readlines()   
    f.close()
acc=c=0
for line in lines:
    c, +=1
    two_ints,num_index =[None]*2,[None] * len(line)
    for i in range(len(word_num)):
        word = word_num[i]
        last_index_found = line.rfind(word)
        if last_index_found != -1:
            num_index[last_index_found] = i 
        first_index_found = line.find(word)
        if first_index_found != -1:
            num_index[first_index_found] = i 
    for i in range(len(line)):
        if line[i].isdecimal():
            num_index[i] = line[i]
    for i in range(len(num_index)):
        if num_index[i]:
            two_ints[0] = 10 * int(num_index[i])
            break
    for i in range(len(num_index)-1,-1,-1):
        if num_index[i]:
            two_ints[1] = int(num_index[i])
            break
    acc+=sum(two_ints)
print(acc,"Acc")
                