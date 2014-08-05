-- Syntax in Functions
-- learnyourhaskell.com/syntax-in-functions

-- pattern matching
lucky :: (Integral a) => a -> String
lucky 7 = "You gave SEVEN"
lucky x = "Sorry, it wasn't what I need."

sayMe :: (Integral a) => a -> String
sayMe 1 = "One"
sayMe 2 = "Two"
sayMe 3 = "Three"
sayMe 4 = "Four"
sayMe 5 = "Five"
sayMe x = "Not between 1 and 5"

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)


charName :: Char -> String
charName 'a' = "Apple"
charName 'b' = "Balloon"
charName 'c' = "Cat"
charName x = "Unknown"

addVectors :: (Num a) => (a,a) -> (a,a) -> (a,a)
addVectors a b = (fst a + fst b, snd a + snd b)

addVectors' :: (Num a) => (a,a) -> (a,a) -> (a,a)
addVectors' (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

first :: (a,b,c) -> a
first (x, _, _) = x

second :: (a,b,c) -> b
second (_, y, _) = y

third :: (a,b,c) -> c
third (_, _, z) = z

listoftuples = [(1,2), (2,3), (3,4), (4,5), (5,6)]
sumall = [ a+b | (a,b) <- listoftuples ]

head' :: [a] -> a
head' [] = error "Cannot do head on empty list"
head' (x:_) = x

tell :: (Show a) => [a] -> String
tell [] = "empty list"
tell (x:[]) = "One element: " ++ show x
tell (x:y:[]) = "Two elements:"  ++ show x ++ " and " ++ show y
tell (x:y:_) = "a long list, but frist two elements are: " ++ show x ++ " and " ++ show y

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs

firstchar :: String -> String
firstchar "" = "Empty"
firstchar all@(x:xs) = "The first character of " ++ all ++ " is " ++ [x]

-- Gaurds

bmiTell :: (RealFloat a) => a -> String
bmiTell bmi
  | bmi <= 18.5 = "Underweight"
  | bmi <= 25.0 = "Normal"
  | bmi <= 30.0 = "Fat"
  | otherwise   = "Obese"

bmiCalc :: (RealFloat a) => a -> a -> String
bmiCalc weight height
  | weight / height ^ 2 <= 18.5 = "Underweight"
  | weight / height ^ 2 <= 25.0 = "Normal"
  | weight / height ^ 2 <= 30.0 = "Fat"
  | otherwise                   = "Obsese"

max' :: (Ord a) => a -> a -> a
max' a b
  | a > b = a
  | otherwise = b

compare' :: (Ord a) => a -> a -> Ordering
a `compare'` b
  | a > b     = GT
  | a == b    = EQ
  | otherwise = LT

bmiCalc' :: (RealFloat a) => a -> a -> String
bmiCalc' weight height
  | bmi <= skinny = "Underweight"
  | bmi <= normal = "Normal"
  | bmi <= fat    = "Fat"
  | otherwise     = "Obese"
  where bmi    = weight / height ^ 2
        skinny = 18.5
        normal = 25.0
        fat    = 30.0

initials :: String -> String -> String
initials fname lname = [f] ++ "." ++ [l] ++ "."
                       where (f:_) = fname
                             (l:_) = lname

calcBMIs :: (RealFloat a) => [(a, a)] -> [a]
calcBMIs xs = [bmi w h | (w, h) <- xs]
              where bmi weight height = weight / height ^ 2

-- Let
-- let <binding> in <expression>

cylinder :: (RealFloat a) => a -> a -> a
cylinder r h =
  let sideArea = 2 * pi * r * h
      topArea = pi * r ^ 2
  in sideArea * 2 + topArea

rescalc = 4 * (let a = 9 in a ^ 2) + 2
squares = [let square x = x * x in (square 5, square 10, square 25)]
squares' = [let square x = x * x in [square m | m <- [1..10]]]
doublelets = (let a = 100; b = 200; c = 300 in a*b*c, let foo="hello"; bar="world" in foo ++ bar)

calcBmis :: (RealFloat a) => [(a, a)] -> [a]
calcBmis xs = [bmi | (w, h) <- xs, let bmi = w / h ^ 2 ]

head'' :: [a] -> a
head'' xs = case xs of [] -> error "No head for empty list"
					   (x:_) -> x
 describeList :: [a] -> String
 describeList xs = "The list is " ++ what xs
 	where what [] = "empty."
 		  what [x] = "is singleton list."
 		  what xs - "a longer list."

