import collections
card_to_counts = collections.defaultdict(lambda: 1)
with open('4.txt') as f:
    for idx, line in enumerate(f):
        card_idx = idx+1
        card_to_counts[card_idx] # ensures original is counted
        win_nums, my_nums = line.split(':')[1].split('|')
        win_nums = [int(num) for num in win_nums.split()]
        my_nums = [int(num) for num in my_nums.split()]
        value = 0 
        for num in win_nums:
            if num in my_nums:
                value += 1        
        for i in range(value):
            card_to_counts[card_idx+i+1] += card_to_counts[card_idx]
print(sum(card_to_counts.values()))