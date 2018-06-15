friends = ['john', 'pat', 'gary', 'michael']

print 'element' , friends[0]


# example 1
for i, name in enumerate(friends):
    print 'element (', i,')', name

# example 2
for friend in friends:
    print 'element', friend


# example 3
i = 0
while i < 10:
    print i
    i+= 1

# Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)
