#insert
a = ["master", "online"]
#name.insert(index, element).
a.insert(1, "code")
print(a)

c = [4, 5, 6]
d = [1, 2, 3]

c.insert(0, d)
print(c)


#sort
company = ["Mateo", "Juan", "Isabel"]
company.sort()
print(company)

#(WHAT IF I TRY IT IN KOREAN???)
bias = ["전호석", "민윤기", "김태형"]
bias.sort()
print(bias)

#SI JALÓ EN COREANO PROFEEE 0_0

#Reverse list
company.sort(reverse=True)
print(company)

#Number of characters 
company.sort(reverse=True, key=len)
