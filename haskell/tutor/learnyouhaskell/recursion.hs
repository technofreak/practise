-- Recursion
-- learnyouhaskell.com/recursion

-- pattern matchin with recursion in where clause
maximum' :: (Ord a) => [a] -> a
maximum' [] = error "maximum for empty list"
maximum' [x] = x
maximum' (x:xs)
	| x > maxTail = x
	| otherwise = maxTail
	where maxTail = maximum' xs

-- pattern matching with recursion and use of max function
maximum'' :: (Ord a) => [a] -> a
maximum'' [] = error "maximum of empty list"
maximum'' [x] = x
maximum'' (x:xs) = max x (maximum'' xs)

-- replicate element x for n times in a list
replicate' :: (Num i, Ord i) => i -> a -> [a]
replicate' n x
	| n <= 0 = []
	| otherwise = x:replicate' (n-1) x

-- take' n x takes n elements from a list x
take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
	| n <= 0 = []
take' _ [] = []
take' n (x:xs) = x:take' (n-1) xs

-- reverse of list x using recursion on tail
reverse' :: [a] => [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

-- infinite list
repeat' :: a -> [a]
repeat' x = x:repeat' x
example = take 3 (repeat' 5)

-- zip using recursion
zip' :: [a] -> [b] -> [(a, b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x, y):zip' xs ys

-- find whether element a is in the list x
elem' :: (Eq a) => a -> [a] -> Bool
elem' a [] = False
elem' a (x:xs)
	| a == x = True
	| otherwise = a `elem'` xs


-- a sorted list is a list that has all the values smalled than or 
-- equal to the head of the list in front, then the head of the list and then 
-- all the values that are bigger than the head
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
	let 
		smallSorted = quicksort [a | a <- xs, a <= x]
		biggerSorted = quicksort [a | a <- xs, a > x]
	in 	smallSorted ++ [x] ++ biggerSorted
