// Logical operators
nott(x) = False if x else True
equals(x,y) = y if x else nott(y)
nequals(x,y) = nott(y) if x else y
andd(x,y) = y if x else False
orr(x,y) = y if nott(x) else True
implies(x,y) = True if nott(x) else y

// All other binary operators
true(x,y) = True
P(x,y) = x
pmi(x,y) = True if x else nott(y)
Q(x,y) = y
nand(x,y) = nott(y) if x else True
notQ(x,y) = nott(y)
nimplies(x,y) = nott(y) if x else False
notP(x,y) = nott(x)
npmi(x,y) = False if x else y
nor(x,y) = False if x else not(y)
false(x,y) = False

// Built in definitions for maths
inc(x) = x+1
dec(x) = x-1
neg(x) = -x
inv(x) = 1.0 / x

// Basic math operations built
add1(x, y) = x if y==0 else add(inc(x), dec(y))
add(x, y) = add1(x, y) if y >= 0 else neg(add1(neg(x), neg(y)))
times1(x, y) = 0 if y==0 else add(x, times1(x, dec(y)))
times(x, y) = times1(x, y) if y >= 0 else neg(times1(x, neg(y)))
exp1(x, y) = 1 if y==0 else times(x, exp(x, dec(y)))
exp(x, y) = exp1(x, y) if y >= 0 else inv(exp1(x, neg(y)))

// Some string manipulation
length(str) = 0 if str=='' else len(str)
chr(str, i) = 'error' if orr(i < 0, i >= length(str)) else str[i]
concat(x, y) = x + '' + y
substr(str, x, y) = '' if x==y else concat(chr(str, x), substr(str, inc(x), y))
rev(str) = '' if str=='' else concat(chr(str, dec(length(str))), rev(substr(str, 0, dec(length(str)))))
nline() = ''

// Main section of program
exp(2,2)
