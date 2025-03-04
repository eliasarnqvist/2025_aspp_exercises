import animals

m = animals.Mammals()
m.printMembers()

# b = animals.Birds()
# b.printMembers()

# f = animals.Fish()
# f.printMembers()

# What is the point of this, are all birds harmless and all fish dangerous?
b = animals.harmless.Birds()
b.printMembers()

f = animals.dangerous.Fish()
f.printMembers()