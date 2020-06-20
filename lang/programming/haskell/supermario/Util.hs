module Util where

-- Utility functions

-- Make pair
pair :: a -> b -> (a, b)
pair a b = (a, b)

-- |Replace i-th element of list to v.
replace :: [a] -> Int -> a -> [a]
replace ls i v = take i ls ++ [v] ++ drop  (i + 1) ls

-- Get last n elements
lastN :: Int -> [a] -> [a]
lastN n xs = supply n [] xs
  where
    supply _ acc [] = acc
    supply 0 acc ys = queue acc ys
    supply m acc (y:ys) = supply (m-1) (acc ++ [y]) ys
    queue acc [] = acc
    queue acc (y:ys) = queue (tail acc ++ [y]) ys

-- Get n width string of base 10
deciWide :: Int -> Char -> Int -> String
deciWide n c = lastN n . (replicate n c ++) . show

-- Add value boundary
rangeadd :: (Num a, Ord a) => a -> a -> a -> a -> a
rangeadd x d x0 x1
  | d > 0 && x < x1  = min (x + d) x1
  | d < 0 && x > x0  = max (x + d) x0
  | otherwise  = x

-- Value goes to 0
friction :: (Num a, Ord a) => a -> a -> a
friction x d
  | x > d    = x - d
  | x < -d  = x + d
  | otherwise  = 0
