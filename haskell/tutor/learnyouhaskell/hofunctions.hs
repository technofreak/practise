-- curried functions

multThree :: (Num a) => a -> a -> a -> a
multThree x y z = x * y * z

-- takes two parameters and multiplies with 9 (9 *)
multWithNine = multThree 9
-- takes one parameter and multiplies with 18 (9 * 2 *)
multWithEighteen = multWithNine 2

compareWithHundred :: (Num a, Ord a) => a -> Ordering
compareWithHundred = compare 100

divideByTen :: (Floating a) => a -> a
divideByTen = (/10)

isUpperAlpha :: Char -> Bool
isUpperAlpha = (`elem` ['A'..'Z'])


-- functions as arguments

callTwice :: (a -> a) -> a -> a
callTwice f x = f (f x)

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f = g
	where g x y = f y x

flip'' :: (a -> b -> c) -> b -> a -> c
flip'' f y x = f x y

-- examples
flipzip = flip' zip [1,2,3,4,5] "hello"
zipflip = zipWith (flip' div) [2,2..] [10,8,6,4,2]

-- maps and filters
map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' p (x:xs)
	| p x = x : filter' p xs
	| otherwise = filter' p xs

-- quicksort with filter
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
	let
		smallerSorted = quicksort (filter (<=x) xs)
		biggerSorted = quicksort (filter (>x) xs)
	in smallerSorted ++ [x] ++ biggerSorted

-- find the largest number under 100000 that is divisible by 3829
largestDivisible :: (Integral a) => a
largestDivisible = head (filter p [100000,99999..])
	where p x = x `mod` 3829 == 0

-- find the sum of all odd squares that are smaller than 10000
sumofoddsquares = sum (takeWhile (<10000) (filter odd (map (^2) [1..])))
sumofoddsquares' = sum (takeWhile (<10000) [n^2 | n <- [1..], odd (n^2)])

-- Collatz sequence
-- take a natural number, if it is even then divide by two, else if odd then
-- multiply by 3 and add 1 to it. take the resulting number and do the same to
-- it. continue doing it to get a chain of numbers. whatever be the starting
-- number, it will finish with 1

chain :: (Integral a) => a -> [a]
chain 1 = [1]
chain n
	| even n = n:chain (n `div` 2)
	| odd n = n:chain (n*3 + 1)

-- for all starting numbers between 1 and 100, how many chains have length
-- greater than 15
numLongChains :: Int
numLongChains = length (filter isLong (map chain [1..100]))
	where isLong xs = length xs > 15


-- Lambdas - anonymous functions

numLongChains' :: Int
numLongChains' = length (filter (\xs -> length xs > 15) (map chain [1..100]))

flip''' :: (a -> b -> c) -> b -> a -> c
flip''' f = \x y -> f y x

-- fold / reduce
sum' :: (Num a) => [a] -> a
sum' xs = foldl (\acc x -> acc + x) 0 xs

sum'' :: (Num a) => [a] -> a
sum'' = foldl (+) 0

elem' :: (Eq a) => a -> [a] -> Bool
elem' y ys = foldl (\acc x -> if x == y then True else acc) False ys

map''' :: (a -> b) -> [a] -> [b]
map''' f xs = foldr (\x acc -> f x : acc) [] xs


-- common functions
exMaximum :: (Ord a) => [a] -> a
exMaximum = foldr1 (\x acc -> if x > acc then x else acc)

exReverse :: [a] -> [a]
exReverse = foldl (\acc x -> x : acc) []

exProduct :: (Num a) => [a] -> a
exProduct = foldr1 (*)

exFilter :: (a -> Bool) -> [a] -> [a]
exFilter p = foldr (\x acc -> if p x then x : acc else acc) []

exHead :: [a] -> a
exHead = foldr1 (\x _ -> x)

exLast :: [a] -> a
exLast = foldl1 (\_ x -> x)


-- how many elements does it take for the sum of the roots of all natural nos
-- to exceed 1000?
sqrtSums :: Int
sqrtSums = length (takeWhile (<1000) (scanl1 (+) (map sqrt [1..]))) + 1

-- Function application with $
sample1 = sum $ filter (> 10) $ map (*2) [2..1]

sample2 = map ($ 3) [(4+), (10*), (^2), sqrt]

-- Function composition
sample3 = map (negate . abs) [5,-3,-6,7,-3,2,-19,-24]

sample4 = map (negate . sum . tail) [[1..5],[3..6],[1..7]]

samplefn = ceiling . negate . tan. cos. max 50

oddSquareSum :: Integer
oddSquareSum = sum . takeWhile (<10000) . filter odd . map (^2) $ [1..]

oddSquareSum' :: Integer
oddSquareSum' =
	let
		oddSquares = filter odd $ map (^2) [1..]
		belowLimit = takeWhile (<10000) oddSquares
	in sum belowLimit

