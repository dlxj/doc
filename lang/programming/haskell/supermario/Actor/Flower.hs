-- Flower

module Actor.Flower (
  newFlower
) where

import Actor (Actor(..))
import Const
import AppUtil (Rect(..), putimg)
import Images
import Player (PlayerType(..), getPlayerType, setPlayerType, addScore)
import Event (Event(..))


data State = Appear | Normal
  deriving (Eq)

data Flower = Flower {
  state :: State,
  cnt :: Int,
  x :: Int,
  y :: Int,
  vx :: Int,
  vy :: Int
  }

instance Actor Flower where
  update _ self =
    case state self of
      Appear  -> updateAppear
      Normal  -> updateNormal
    where
      updateNormal = (self, [])
      updateAppear = (self', [])
        where
          self' = self { y = y self - one `div` 2, state = state', cnt = cnt self + 1 }
          state' = if cnt self < 32 then Appear else Normal

  render self imgres scrx sur =
    putimg sur imgres ImgFlower ((x self) `div` one - chrSize `div` 2 - scrx) ((y self) `div` one - 15 - 8)

  getHitRect self =
    if state self == Normal then rect else Nothing
    where
      rect = Just $ Rect (xx - 8) (yy - 16) (xx + 8) yy
      xx = x self `div` one
      yy = y self `div` one

  onHit pl self = (addScore pointFlower $ setPlayerType nt pl, Nothing, ev)
    where
      nt = case pltype of
        SmallMonao  -> SuperMonao
        SuperMonao  -> FireMonao
        _      -> pltype
      pltype = getPlayerType pl
      ev = [EvScoreAddEfe (x self `div` one) (y self `div` one - chrSize * 2) pointFlower]


newFlower :: Int -> Int -> Flower
newFlower cx cy =
  Flower { state = Appear, cnt = 0, x = cx * chrSize * one + chrSize * one `div` 2, y = (cy+1) * chrSize * one, vx = one, vy = 0 }
