-- Mushroom (power up item)

module Actor.Kinoko (
  newKinoko
) where

import Actor (Actor(..))
import Actor.Common (updateActorBase)
import AppUtil (Rect(..), putimg)
import Const
import Images
import Player (PlayerType(..), getPlayerType, setPlayerType, addScore)
import Event (Event(..))

ofsH :: Int
ofsH = 15

data State = Appear | Normal
  deriving (Eq)

data Kinoko = Kinoko {
  state :: State,
  cnt :: Int,
  x :: Int,
  y :: Int,
  vx :: Int,
  vy :: Int
  }

instance Actor Kinoko where
  update fld self =
    case state self of
      Appear  -> updateAppear
      Normal  -> updateNormal
    where
      updateNormal = (self', [])
        where
          self' = self { x = x', y = y', vx = vx', vy = vy' }
          (x', y', vx', vy') = updateActorBase fld (x self, y self, vx self, vy self)
      updateAppear = (self', [])
        where
          self' = self { y = y self - one `div` 2, state = state', cnt = cnt self + 1 }
          state' = if cnt self < 32 then Appear else Normal

  render self imgres scrx sur =
    putimg sur imgres ImgKinoko ((x self) `div` one - chrSize `div` 2 - scrx) ((y self) `div` one - ofsH - 8)

  bDead self = y self >= (screenHeight + chrSize * 3) * one || x self <= -chrSize * one

  getHitRect self =
    if state self == Normal then rect else Nothing
    where
      rect = Just $ Rect (xx - 8) (yy - 16) (xx + 8) yy
      xx = x self `div` one
      yy = y self `div` one

  onHit pl self = (addScore pointKinoko $ setPlayerType nt pl, Nothing, ev)
    where
      nt = case typ of
        SmallMonao  -> SuperMonao
        SuperMonao  -> FireMonao
        _      -> typ
      typ = getPlayerType pl
      ev = [EvScoreAddEfe (x self `div` one) (y self `div` one - chrSize * 2) pointKinoko]

newKinoko :: Int -> Int -> Kinoko
newKinoko cx cy =
  Kinoko { state = Appear, cnt = 0, x = cx * chrSize * one + chrSize * one `div` 2, y = (cy+1) * chrSize * one, vx = one, vy = 0 }
