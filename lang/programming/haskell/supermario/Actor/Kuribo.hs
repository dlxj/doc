﻿-- Kuribo

module Actor.Kuribo (
  newKuribo
) where

import Actor (Actor(..), ActorWrapper(..))
import Actor.Common (updateActorBase, stamp)
import AppUtil (Rect(..), putimg)
import Const
import Images
import Player (setPlayerDamage, stampPlayer, addScore)
import Event (Event(..))

ofsH :: Int
ofsH = 15

data Kuribo = Kuribo {
  x :: Int,
  y :: Int,
  vx :: Int,
  vy :: Int,
  cnt :: Int
  }

instance Actor Kuribo where
  update fld self = (self', [])
    where
      self' = self { x = x', y = y', vx = vx', vy = vy', cnt = cnt self + 1 }
      (x', y', vx', vy') = updateActorBase fld (x self, y self, vx self, vy self)

  render self imgres scrx sur =
    putimg sur imgres imgtype (x self `div` one - chrSize `div` 2 - scrx) (y self `div` one - ofsH - 8)
    where
      imgtype = [ImgKuri0, ImgKuri1] !! (cnt self `mod` 16 `div` 8)

  bDead self = y self >= (screenHeight + chrSize * 3) * one || x self <= -chrSize * one

  getHitRect self = Just $ Rect (xx - 8) (yy - 16) (xx + 8) yy
    where
      xx = x self `div` one
      yy = y self `div` one

  onHit pl self
    | stamp pl (x self, y self)  = (addScore pointKuribo $ stampPlayer pl, Just $ ActorWrapper $ newStampedKuribo (x self `div` one - chrSize `div` 2) (y self `div` one), ev)
    | otherwise  = (setPlayerDamage pl, Just $ ActorWrapper self, [])
    where
      ev = [EvScoreAddEfe (x self `div` one) (y self `div` one - chrSize * 2) pointKuribo]

newKuribo :: Int -> Int -> Kuribo
newKuribo cx cy =
  Kuribo { x = cx * chrSize * one + chrSize * one `div` 2, y = (cy+1) * chrSize * one, vx = -one `div` 2, vy = 0, cnt = 0 }


-- Stamped Kuribo
data StampedKuribo = StampedKuribo {
  sx :: Int,
  sy :: Int,
  ccnt :: Int
  }

instance Actor StampedKuribo where
  update _ self = (self { ccnt = ccnt self + 1 }, [])

  render self imgres scrx sur =
    putimg sur imgres ImgKuriDead (sx self - scrx) (sy self - 7 - 8)

  bDead self = ccnt self >= frameRate `div` 2

newStampedKuribo :: Int -> Int -> StampedKuribo
newStampedKuribo sx' sy' = StampedKuribo { sx = sx', sy = sy', ccnt = 0 }
