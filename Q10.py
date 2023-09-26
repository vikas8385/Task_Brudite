input_list =[1,2,3,2,4,1,2,5,5]
freq_count={}
for element in input_list:
    if element in freq_count:
        freq_count[element] += 1
    else:
        freq_count[element] = 1

print("Frequence count:",freq_count)
