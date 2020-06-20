{-# LANGUAGE ScopedTypeVariables #-}
module Mixer (
  initMixer,
  playSE,
  playBGM,
  stopBGM
) where

import Control.Exception
import Graphics.UI.SDL.Mixer
import Data.IORef (IORef, newIORef, readIORef, writeIORef)
import System.IO.Unsafe (unsafePerformIO)

freq, channel, samples :: Int
format :: AudioFormat

freq = 22050
format = AudioS16Sys
channel = 2
samples = 4096

initMixer :: IO ()
initMixer = do
  openAudio freq format channel samples

playSE :: Maybe Chunk -> IO ()
playSE Nothing = return ()
playSE (Just ad) = flip catch (\(_ :: SomeException) -> return ()) $ do
  playChannel (-1) ad 0
  return ()

playingBGM :: IORef (Maybe Music)
playingBGM = unsafePerformIO $ newIORef Nothing

stopBGM :: IO ()
stopBGM = do
  m <- readIORef playingBGM
  case m of
    Nothing -> return ()
    Just mus -> do
      freeMusic mus
      writeIORef playingBGM Nothing

playBGM :: String -> IO ()
playBGM bgmfn = do
  stopBGM
  maybeMusic <- tryLoadMUS bgmfn
  case maybeMusic of
    Just music -> do
      playMusic music (-1)
      writeIORef playingBGM $ Just music
    Nothing -> return ()
