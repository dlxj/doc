﻿-- Block bounce animation

module Actor.AnimBlock (
  newAnimBlock
) where

import Actor (Actor(..))
import AppUtil (cellCrd, putimg)
import Const
import Field (Cell, chr2img)
import Event (Event(..))


data AnimBlock = AnimBlock {
  startcy :: Int,
  x :: Int,
  y :: Int,
  vy :: Int,
  chr :: Cell
  }

instance Actor AnimBlock where
  update _ self
    | not (bDead self)  = (self', ev')
    | otherwise      = (self, [])

    where
      vy' = vy self + gravity
      y' = y self + vy'
      self' = self { vy = vy', y = y' }
      ev' = if bDead self'
        then [EvSetField (cellCrd $ x self) (startcy self) $ chr self]
        else []

  render self imgres scrx sur =
    putimg sur imgres (chr2img $ chr self) (x self `div` one - scrx) (y self `div` one - 8)

  bDead self = vy self > 0 && y self >= startcy self * chrSize * one

newAnimBlock :: Int -> Int -> Cell -> AnimBlock
newAnimBlock cx cy c =
  AnimBlock { startcy = cy, x = cx * chrSize * one, y = cy * chrSize * one, vy = -3 * one, chr = cc }
  where
    cc = case c of
      '?'  -> '#'
      'K'  -> '#'
      o  -> o
