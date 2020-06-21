-- Common action

module Actor.Common (
  updateActorBase,
  stamp
) where

import Const
import Field
import AppUtil (cellCrd)
import Player (Player, getPlayerVY)


-- Common action
{-
  Move horizontally, turn when hit wall, fall when no floor.
-}
updateActorBase :: Field -> (Int, Int, Int, Int) -> (Int, Int, Int, Int)
updateActorBase fld (x, y, vx, vy)
  | isGround  = (x', groundy', vx', 0)
  | otherwise  = (x', y', vx', vy')
  where
    x' = x + vx
    sideWall = isBlock $ fieldRef fld (cellCrd $ x' + signum vx * 6 * one) (cellCrd $ y - chrSize * one `div` 2)
    vx'
      | sideWall  = -vx
      | otherwise  = vx

    vy' = min maxVy $ vy + gravity
    y' = y + vy'
    isGround = isBlock $ fieldRef fld (cellCrd $ x') (cellCrd y')
    groundy' = (cellCrd y') * one * chrSize


-- Stamp by player?
stamp :: Player -> (Int, Int) -> Bool
stamp pl (_,_) = getPlayerVY pl > 0
