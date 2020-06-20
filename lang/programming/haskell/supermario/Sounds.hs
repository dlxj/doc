module Sounds (
  SoundType(..), soundTypes, soundFn
  , BGMType(..), bgmFn
) where

data SoundType =
    SndJump
  |  SndShot
  |  SndPunch
  |  SndBreak
  |  SndCoin
  deriving (Eq, Show)

soundTypes :: [SoundType]
soundTypes = [SndJump, SndShot, SndPunch, SndBreak, SndCoin]

soundFn :: SoundType -> String
soundFn SndJump = "hoyo.wav"
soundFn SndShot = "suiteki.wav"
soundFn SndPunch = "po2.wav"
soundFn SndBreak = "cha.wav"
soundFn SndCoin = "puni.wav"


data BGMType =
    BGMMain
  deriving (Eq, Show)

bgmFn :: BGMType -> String
bgmFn BGMMain = "main.mp3"
