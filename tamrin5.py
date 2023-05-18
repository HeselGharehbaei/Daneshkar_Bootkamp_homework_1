
laptop_price_quality = list(map(int, input("input price, quality:").split(", " )))
price_list = laptop_price_quality[::2]
quality_list = laptop_price_quality[1::2]
result = ""
range_price_quality = range(len(price_list))
for i in range_price_quality:
    for j in range_price_quality:
        if  price_list[i] <= price_list[j] and quality_list[i] >= quality_list[j]:
            result = "Founded"
            break 
    if  result == "Founded":
        print("Founded")
        break
else:
    print("NotFounded")                       
