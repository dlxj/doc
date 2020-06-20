-- Player (monao)

module Player (
  Player,
  PlayerType(..),
  newPlayer,
  updatePlayer,
  renderPlayer,
  playerGetCoin,
  addScore,
  getScrollPos,
  getPlayerX,
  getPlayerY,
  getPlayerVY,
  getPlayerHitRect,
  getPlayerCoin,
  getPlayerScore,
  getPlayerType,
  setPlayerType,
  setPlayerDamage,
  stampPlayer,
  getPlayerDead
) where

import Graphics.UI.SDL (Surface)
import Data.Bits ((.&.))

import Util
import AppUtil (ImageResource, cellCrd, Rect(..), putimg)
import Pad
import Const
import Images
import Field
import Event
import Actor (ActorWrapper(..))
import Actor.Shot
import Sounds

walkVx, runVx, acc, acc2, jumpVy, jumpVy2, scrollMinX, scrollMaxX, gravity2, stampVy, undeadFrame :: Int
walkVx = one * 4 `div` 2
runVx = one * 11 `div` 4
acc = one `div` 32
acc2 = one `div` 14
jumpVy = -12 * gravity
jumpVy2 = -13 * gravity
scrollMinX = 5 * chrSize + 6
scrollMaxX = 8 * chrSize
gravity2 = one `div` 6    -- gravity when falling and pressing A btn
stampVy = -8 * gravity
undeadFrame = frameRate * 2

-- Type of player
data PlayerType = SmallMonao | SuperMonao | FireMonao
  deriving (Eq)

-- State
data PlayerState = Normal | DeadFall | Dead
  deriving (Eq)

-- Structure
data Player = Player {
  pltype :: PlayerType,
  plstate :: PlayerState,
  x :: Int,
  y :: Int,
  vx :: Int,
  vy :: Int,
  scrx :: Int,
  stand :: Bool,
  undeadCount :: Int,

  coin :: Int,
  score :: Int,

  lr :: Int,
  pat :: Int,
  anm :: Int
  }

newPlayer :: Player
newPlayer = Player {
  pltype = SmallMonao,
  plstate = Normal,
  x = 3 * chrSize * one,
  y = 13 * chrSize * one,
  vx = 0,
  vy = 0,
  scrx = 0,
  stand = False,
  undeadCount = 0,

  coin = 0,
  score = 0,

  lr = 1,
  pat = 0,
  anm = 0
  }


patStop, patWalk, walkPatNum, patJump, patSlip, patSit, patShot, patDead :: Int
patStop = 0
patWalk = 1
walkPatNum = 3
patJump = patWalk + walkPatNum
patSlip = patJump + 1
patSit = patSlip + 1
patShot = patSit + 1
patDead = patShot + 1

imgTableSmall, imgTableSuper, imgTableFire :: [[ImageType]]
imgTableSmall = [
  [ImgMonaoLStand, ImgMonaoLWalk1, ImgMonaoLWalk2, ImgMonaoLWalk3, ImgMonaoLJump, ImgMonaoLSlip, ImgMonaoLStand, ImgMonaoLStand, ImgMonaoDead],
  [ImgMonaoRStand, ImgMonaoRWalk1, ImgMonaoRWalk2, ImgMonaoRWalk3, ImgMonaoRJump, ImgMonaoRSlip, ImgMonaoRStand, ImgMonaoLStand, ImgMonaoDead]
  ]
imgTableSuper = [
  [ImgSMonaoLStand, ImgSMonaoLWalk1, ImgSMonaoLWalk2, ImgSMonaoLWalk3, ImgSMonaoLJump, ImgSMonaoLSlip, ImgSMonaoLSit],
  [ImgSMonaoRStand, ImgSMonaoRWalk1, ImgSMonaoRWalk2, ImgSMonaoRWalk3, ImgSMonaoRJump, ImgSMonaoRSlip, ImgSMonaoRSit]
  ]
imgTableFire = [
  [ImgFMonaoLStand, ImgFMonaoLWalk1, ImgFMonaoLWalk2, ImgFMonaoLWalk3, ImgFMonaoLJump, ImgFMonaoLSlip, ImgFMonaoLSit, ImgFMonaoLShot],
  [ImgFMonaoRStand, ImgFMonaoRWalk1, ImgFMonaoRWalk2, ImgFMonaoRWalk3, ImgFMonaoRJump, ImgFMonaoRSlip, ImgFMonaoRSit, ImgFMonaoRShot]
  ]


-- Move horizontal
moveX :: Pad -> Player -> Player
moveX pad self =
  if stand self
    then self' { lr = lr', pat = pat', anm = anm' }
    else self'
  where
    axtmp = if padd then 0 else (-padl + padr) * nowacc
    ax = if signum (axtmp * vx self) < 0 then axtmp * 2 else axtmp
    vx'
      | ax /= 0      = rangeadd (vx self) ax (-maxspd) maxspd
      | stand self    = friction (vx self) acc
      | otherwise      = vx self
    x' = max xmin $ (x self) + vx'

    padd = if pressing pad padD then True else False
    padl = if pressing pad padL then 1 else 0
    padr = if pressing pad padR then 1 else 0
    maxspd
      | not $ stand self  = walkVx `div` 2
      | pressing pad padB  = runVx
      | otherwise        = walkVx
    nowacc
      | pressing pad padB  = acc2
      | otherwise        = acc
    xmin = (scrx self + chrSize `div` 2) * one

    self' = self { x = x', vx = vx' }

    lr' =
      case (-padl + padr) of
        -1  -> 0
        1  -> 1
        _  -> lr self
    pat'
      | padd && pltype self /= SmallMonao  = patSit
      | vx' == 0        = patStop
      | vx' > 0 && lr' == 0  = patSlip
      | vx' < 0 && lr' == 1  = patSlip
      | otherwise        = (anm' `div` anmCnt) + patWalk
    anm'
      | vx' == 0    = 0
      | otherwise    = ((anm self) + (abs vx')) `mod` (walkPatNum * anmCnt)
    anmCnt = walkVx * 3

-- Check wall for moving horizontal direction
checkX :: Field -> Player -> Player
checkX fld self
  | dir == 0  = check (-1) $ check 1 $ self
  | otherwise = check dir $ self
  where
    dir = signum $ vx self
    check dx self'
      | isBlock $ fieldRef fld cx cy  = self' { x = (x self') - dx * one, vx = 0 }
      | otherwise            = self'
      where
        cx = cellCrd (x self' + ofsx dx)
        cy = cellCrd (y self' - chrSize `div` 2 * one)
        ofsx 1 =  5 * one
        ofsx _ = -6 * one

-- Adjust horizontal scroll position
scroll :: Player -> Player -> Player
scroll opl self = self { scrx = scrx' }
  where
    odx = x opl `div` one - scrx opl
    dx = (max 0 $ vx self) * (scrollMaxX - scrollMinX) `div` runVx + scrollMinX
    scrx'
      | d > 0    = scrx self + d
      | otherwise  = scrx self
    d = x self `div` one - scrx self - (max odx dx)


-- Fall by gravity
fall :: Bool -> Player -> Player
fall abtn self
  | stand self  = self
  | otherwise    = self { y = y', vy = vy' }
  where
    ay
      | vy self < 0 && abtn  = gravity2
      | otherwise        = gravity
    vy' = min maxVy $ vy self + ay
    y' = y self + vy'


-- Check for stand on a floor
checkFloor :: Field -> Player -> Player
checkFloor fld self
  | stand'  = self { stand = stand', y = ystand, vy = 0 }
  | otherwise  = self { stand = stand' }
  where
    stand'
      | vy self >= 0  = isGround (-6) || isGround 5
      | otherwise      = stand self
    ystand = (cellCrd $ y self) * (chrSize * one)

    isGround ofsx = isBlock $ fieldRef fld (cellCrd $ x self + ofsx * one) (cellCrd (y self))

-- Check upper wall
checkCeil :: Field -> Player -> (Player, [Event])
checkCeil fld self
  | stand self || vy self >= 0 || not isCeil  = (self, [])
  | otherwise = (self { y = y', vy = 0 }, [EvHitBlock ImgBlock2 cx cy (pltype self /= SmallMonao), EvSound SndBreak])
  where
    yofs = case pltype self of
      SmallMonao  -> 14
      SuperMonao  -> 28
      FireMonao  -> 28
    ytmp = y self - yofs * one

    cx = cellCrd $ x self
    cy = cellCrd ytmp
    isCeil = isBlock $ fieldRef fld cx cy
    y' = ((cy + 1) * chrSize + yofs) * one

-- Do jump?
doJump :: Pad -> Player -> (Player, [Event])
doJump pad self
  | stand self && justPressed pad padA  = (self { vy = vy', stand = False, pat = patJump }, [EvSound SndJump])
  | otherwise              = (self, [])
  where
    vy' = (jumpVy2 - jumpVy) * (abs $ vx self) `div` runVx + jumpVy


-- Do shot?
shot :: Pad -> Player -> (Player, [Event])
shot pad self
  | canShot && justPressed pad padB  = (shotPl, shotEv)
  | otherwise            = (self, [])
  where
    canShot = pltype self == FireMonao
    shotPl = self { pat = patShot }
    shotEv = [  EvAddActor $ ActorWrapper $ newShot (x self) (y self) (lr self),
          EvSound SndShot
        ]


-- Update
updatePlayer :: Pad -> Field -> Player -> (Player, [Event])
updatePlayer pad fld self =
  case plstate self of
    Normal    -> updateNormal pad fld self'
    DeadFall  -> updateDeadFall pad fld self'
    Dead    -> updateDead pad fld self'
  where
    self' = decUndead self
    decUndead pl = pl { undeadCount = max 0 $ undeadCount pl - 1 }

-- In normal state
updateNormal :: Pad -> Field -> Player -> (Player, [Event])
updateNormal pad fld self = (self3, ev1 ++ ev2 ++ ev3)
  where
    (self1, ev1) = moveY $ scroll self $ checkX fld $ moveX pad self
    (self2, ev2) = checkCeil fld self1
    (self3, ev3) = shot pad self2
    moveY = doJump pad . checkFloor fld . fall (pressing pad padA)

-- In dead state
updateDeadFall :: Pad -> Field -> Player -> (Player, [Event])
updateDeadFall _ _ self = (fall False self, [])

-- In dead state
updateDead :: Pad -> Field -> Player -> (Player, [Event])
updateDead _ _ self = (fall False self, [])

-- Get scroll position
getScrollPos :: Player -> Int
getScrollPos = scrx

-- Get x position
getPlayerX :: Player -> Int
getPlayerX = x

-- Get Y position
getPlayerY :: Player -> Int
getPlayerY = y

-- Get y velocity
getPlayerVY :: Player -> Int
getPlayerVY = vy

-- Get hit rect
getPlayerHitRect :: Player -> Rect
getPlayerHitRect self = Rect (xx - 6) (yy - 16) (xx + 6) yy
  where
    xx = x self `div` one
    yy = y self `div` one

-- Get coin num
getPlayerCoin :: Player -> Int
getPlayerCoin = coin

-- Get score
getPlayerScore :: Player -> Int
getPlayerScore = score

-- Get type
getPlayerType :: Player -> PlayerType
getPlayerType = pltype

-- Set type
setPlayerType :: PlayerType -> Player -> Player
setPlayerType t self = self { pltype = t }

-- Set damage
setPlayerDamage :: Player -> Player
setPlayerDamage self
  | undeadCount self > 0      = self
  | pltype self == SmallMonao    = self { pltype = SmallMonao, plstate = DeadFall, pat = patDead, vy = jumpVy, stand = False }
  | otherwise            = self { pltype = SmallMonao, undeadCount = undeadFrame }

-- Stamp enemy
stampPlayer :: Player -> Player
stampPlayer self = self { vy = stampVy }

-- Player get a coin
playerGetCoin :: Player -> Player
playerGetCoin self = self { coin = (coin self + 1) `mod` 100 }

-- Add score
addScore :: Int -> Player -> Player
addScore a self = self { score = score self + a }

-- Player is dead?
getPlayerDead :: Player -> Bool
getPlayerDead self =
  plstate self /= Normal

-- Render
renderPlayer :: Surface -> ImageResource -> Int -> Player -> IO ()
renderPlayer sur imgres scrx_ self = do
  if undeadCount self == 0 || (undeadCount self .&. 1) /= 0
    then putimg sur imgres imgtype sx posy
    else return ()
  where
    posy = case pltype self of
      SmallMonao  -> sy - chrSize + 1
      _      -> sy - chrSize * 2 + 1
    imgtype
      | plstate self == Dead  = ImgMonaoDead
      | otherwise        = imgtbl !! lr self !! pat self
    imgtbl = case pltype self of
      SmallMonao  -> imgTableSmall
      SuperMonao  -> imgTableSuper
      FireMonao  -> imgTableFire
    sx = x self `div` one - chrSize `div` 2 - scrx_
    sy = y self `div` one - 8
