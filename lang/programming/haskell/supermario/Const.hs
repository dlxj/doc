module Const where

-- Window
wndTitle :: String
wndTitle = "Monao in Haskell"

screenWidth, screenHeight, wndBpp, frameRate :: Int
screenWidth = 256
screenHeight = 224
wndBpp = 32

frameRate = 60

-- Game timer
timeBase :: Int
timeBase = 22


-- One for fixed point integer
one :: Int
one = 256

-- Size of charcter
chrSize :: Int
chrSize = 16

-- Gravity
gravity :: Int
gravity = one * 2 `div` 5

-- Maximum speed for falling
maxVy :: Int
maxVy = one * 5


-- Score point
pointKuribo, pointNokonoko, pointKinoko, pointFlower, pointBreakBlock, pointGetCoin, pointKoura :: Int
pointKuribo    = 100
pointNokonoko  = 100
pointKinoko    = 1000
pointFlower    = 1000
pointBreakBlock  = 50
pointGetCoin  = 200
pointKoura    = 400
