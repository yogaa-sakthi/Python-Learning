a=[1,2,3,4]
b=[5,6]
a[0]=11
a.pop(3)
a.extend(b)
a.insert(3,5)
a.append(8)
print("list",a)


a=(1,2,4,5)
print(type(a))

a=(1,2,4,5)
b=list(a)
print(b)

a={2,4,5}
a.add(6)
a.remove(4)


a={"name":"emc"}
print(a["name"])
