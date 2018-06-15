
name = raw_input('What is your name?\n')
# name = 'joel'

print "joel" + " " + "gonzales"

print 'My name is %s' % name

var1 = "form1"
var2 = "form2"

print "First is %s, second is %s" % (var1, var2)

# string concatenation
name1 = "joel"
lastname = "gonzales"

print name1,lastname

# string interpolation

# 2.x
result = "my {0} string: {1}".format("cool", "Hello there!")
print result

name = "Spongebob Squarepants"
print("Who lives in a Pineapple under the sea? %(name)s." % locals())

# 3.6
# name = "Spongebob Squarepants"
# print(f"Who lives in a Pineapple under the sea? {name}.")
