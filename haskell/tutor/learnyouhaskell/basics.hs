-- Basics
-- Refer: learnyourhaskell.com/starting-out

doubleMe x = x + x

doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100
						then x
						else x*2

listofNumbers = [4,8,16,24,42]

concatList = [1,2,3] ++ [4,5,6]
concatWord = "Hello" ++ " " ++ "world!"
concatChars = ['h','e'] ++ ['l','l','o']

appendChar = 'A':" Small Car"
appendNum = 5:[1,2,3,4]

fourthNum = listofNumbers !! 4

cmp1 = [3,2,1] > [2,1,0]
cmp2 = [3,2,1] > [2,10,100]
cmp3 = [3,2,1] == [3,2,1]

headofList = head listofNumbers
tailoflist = tail listofNumbers
lastoflist = last listofNumbers
initoflist = init listofNumbers
lenoflist = length listofNumbers
isnull = null listofNumbers
revlist = reverse listofNumbers
extract3 = take 3 listofNumbers
extractnone = take 0 listofNumbers
drop3 = drop 3 listofNumbers
maxoflist = maximum listofNumbers
minoflist = minimum listofNumbers
sumoflist = sum listofNumbers
prodoflist = product listofNumbers
checkelem = 24 `elem` listofNumbers

rangeofnum = [1..20]
rangeofalphab = ['a'..'z']
evennos = [2,4..20]
multiplesof7 = take 10 [7,14..]
cyclelist = take 5 (cycle [1,2,3])
repeatnum = take 10 (repeat 5)
replicatenum = replicate 3 10

doubleX = [x*2 | x <- [1..10]]
doubleXGrThan12 = [x*2 | x <- [1..10], x*2 >= 12]
divby7gives3 = [x | x <- [50..100], x `mod` 7 == 3]
boomBangs xs = [ if x < 10 then "boom!" else "bang!" | x <- xs, odd x]
printboombangs = boomBangs [1..13]
selectiveignores = [x | x <- [1..10], x /= 3, x /= 7, x /= 9]

multilists = [x*y | x <- [2,4,6,8], y <- [3,5,7,9], x*y > 10]
nouns = ["dog","cow","tiger"]
verbs = ["barking","milking","hunting"]
combinewords = [verb ++ " " ++ noun | verb <- verbs, noun <- nouns]

length' xs  = sum [1| _ <- xs]
reslen = length' [1,2,3,4,5]

retainUpper st = [c | c <- st, c `elem` ['A'..'Z']]
resstr = retainUpper "AbacadaBRa"

xxs = [[1,3,5,7,9,11,13],[2,4,6,8,10,12],[1,2,3,4,5,6]]
resxxs = [ [x | x <- xs, even x] | xs <- xxs]

atuple = (1, "one")
alistoftuples = [(1, "one"), (2, "two"), (3, "three")]
first = fst atuple
second = snd atuple

zipped = zip [1..5] ["one","two","three","four","five"]

triangles = [ (a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10] ]
righttriangles = [ (a,b,c) | c <- [1..10], b <- [1..10], a <- [1..10], a^2 + b^2 == c^2, a+b+c == 24 ]
