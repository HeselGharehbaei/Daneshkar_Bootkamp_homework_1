
string = input("string =")
count_repeat_items = dict.fromkeys(string, 0)
for item in string:
    count_repeat_items[item]+=1
print(count_repeat_items)  
