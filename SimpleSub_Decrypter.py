common = 'etaoinsrhldcumfpgwybvkxjqz'
lfreq = {}

ctext = input("Please enter the cipher text\n")
lowered = ctext.lower()

for key in lowered:
    if key == " ":
        continue
    else:
        lfreq[key] = lfreq.get(key, 0) + 1

sortedfreq = {k: v for k, v in sorted(lfreq.items(), key=lambda item: item[1], reverse=True)}


count = 0
temp = lowered
for element in sortedfreq:
    i=0
    for char in lowered:
        if char == element:
            temp = temp[:i] + common[count] + temp[i+1:]
        i+=1
    count += 1
    #temp = temp.replace(element, common[count])
    
#print("Count of all characters in the cipher text is : \n" +  str(lfreq))
#for i in sortedfreq:
#    print(i[0])
print("cyphertext: " + ctext)
print("plaintext: " + temp)

