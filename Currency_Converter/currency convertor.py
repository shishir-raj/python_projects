with open('currency.txt') as f:
    lines=f.readlines()
# print(lines)  #print all the lines of the file  or whole file
currency_dict={}
for line in lines:      #for loop to print line by line
    parse=line.split("\t")  #it splits the line where \t occur (or where ,)
    currency_dict[parse[0]]=parse[1]
# print(currency_dict)

amount=int(input("Enter the Amount: "))
print("Enter the name of currency in which you want to convert: ")
#
for item in currency_dict.keys():
    print(item)

# [print(item)for item in currency_dict.keys()]
#
currency = input("Enter the country name from the above list = ")
print(f'{amount} in INR = {amount * float(currency_dict[currency])} {currency}')