-- Types and Typeclasses
-- Refer: learnyourhaskell.com/types-and-typeclasses

-- type
-- :t 'a'
-- -- 'a' :: char
-- :t True
-- -- True : Bool
-- :t "Hello"
-- -- "Hello" :: [Char]
-- :t (True, 'a')
-- -- (True, 'a') :: (Bool, Char)

-- explicit type declaration
removeNonUpperCase :: [Char] -> [Char]
removeNonUpperCase st = [ c | c <- st, c `elem` ['A'..'Z'] ]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

-- common types
-- Int dounded integer
-- Integer unbounded integer
factorial :: Integer -> Integer
factorial n = product [1..n]
-- Float single precision
circumference :: Float -> Float
circumference r = 2 * pi * r
-- circumference 4.0 -- 25.132742
-- Double double precision
circumference' :: Double -> Double
circumference' r = 2 * pi * r
-- circumference 4.0 -- 25.132741228718346
-- Bool
-- Char

-- type variables
-- :t head
-- -- head :: [a] -> a
-- :t fst
-- -- head :: (a, b) -> a

-- typeclasses

-- :t (==)
-- (==) :: (Eq a) => a -> a -> Bool
-- Eq typeclass provides an interface to test equality
-- All standard Haskell types except IO and functions are part of Eq
-- Its members implement are == and /=

-- Ord for types that have an ordering
-- :t (>)
-- (>) :: (Ord a) => a -> a -> Bool
-- all types except functions are part of Ord
-- covers > < >= <=
-- Example: compare function takes two Ord members and returns Ordering 
-- (LT, GT, EQ)
-- "Apple" `compare` "Orange"
-- LT

-- Show

-- Read
-- :t read
-- read :: (Read a) => String -> a
-- read "True" || False
-- True
-- read "5" + 2.0
-- 7.0
-- read "[1,2,3,4]" + [5]
-- [1,2,3,4,5]
-- type annotation - explicit way of telling the type of an expression
-- read "5" :: Int
-- 5
-- (read "5" :: Float) * 4
-- 20.0
-- read "[1,2,3,4]" :: [Int]
-- [1,2,3,4]

-- Enum - sequentially ordered types
-- succ and pred functions
-- Types: (), Bool, Char, Ordering, Int, Integer, Float, Double
-- ['a'..'z']
-- [LT..GT]
-- succ 6

-- Bounded - members have a lower and upper bound
-- Int, Char, Bool

-- Num - polymorphic constants
-- :t 20
-- 20 :: (Num t) => t
-- 20 :: Int
-- 20
-- 20 :: Integer
-- 20
-- 20 :: Float
-- 20.0
-- 20 :: Double
-- 20.0
-- :t (*)
-- (*) :: (Num, a) => a -> a -> a

-- Integral - Int and Integer
-- Floating - Float and Double