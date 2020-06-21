{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE ForeignFunctionInterface #-}
module AppUtil (
  KeyProc,
  getKeyState,
  key2btn,

  delayedStream,
  procSDLEvent,

  ImageResource,
  loadImageResource,
  releaseImageResource,
  getImageSurface,
  putimg,

  SoundResource,
  loadSoundResource,
  bgmPath,

  cellCrd,
  Rect(..),
  ishit
) where

import Control.Exception
import Graphics.UI.SDL hiding (flip)
import Graphics.UI.SDL.Utilities
import Graphics.UI.SDL.Mixer
import Data.Maybe (fromJust)
import Data.List (findIndices)
import System.IO.Unsafe (unsafePerformIO,unsafeInterleaveIO)
import Foreign
import Foreign.C.Types
import Pad
import Const
import Images
import Sounds

imagePath, soundPath, bgmPath :: String
imagePath = "data/img/"
soundPath = "data/snd/"
bgmPath = "data/snd/"

-- `SDL_GetKeyState' is not defined in Graphic.UI.SDL
foreign import ccall unsafe "SDL_GetKeyState" sdlGetKeyState :: Ptr CInt -> IO (Ptr Word8)

type KeyProc = SDLKey -> Bool

-- Get keyboard state and return function
getKeyState :: IO KeyProc
getKeyState = alloca $ \numkeysPtr -> do
  keysPtr <- sdlGetKeyState numkeysPtr
  if True
    then do    -- for anarchy: Use unsafePerformIO
      let f = \k -> (/= 0) $ unsafePerformIO $ (peekByteOff keysPtr $ fromIntegral $ Graphics.UI.SDL.Utilities.fromEnum k :: IO Word8)
      return f
    else do    -- for conservative
      numkeys <- peek numkeysPtr
      keys <- (map Graphics.UI.SDL.Utilities.toEnum . map fromIntegral . findIndices (== 1)) `fmap` peekArray (fromIntegral numkeys) keysPtr
      return $ (`elem` keys)

key2btn :: KeyProc -> Int
key2btn ks = foldl (\r -> (r .|.) . uncurry press) 0 btns
  where
    btns = [
      (padU, [SDLK_UP, SDLK_i]),
      (padD, [SDLK_DOWN, SDLK_k]),
      (padL, [SDLK_LEFT, SDLK_j]),
      (padR, [SDLK_RIGHT, SDLK_l]),
      (padA, [SDLK_SPACE, SDLK_z]),
      (padB, [SDLK_LSHIFT, SDLK_RSHIFT])
      ]
    press v ls = if any ks ls then v else 0

-- Delayed stream
-- return result list of action, interval microsec
delayedStream :: Int -> IO a -> IO [a]
delayedStream microsec func = unsafeInterleaveIO $ do
  Graphics.UI.SDL.delay $ Prelude.toEnum $ microsec `div` 1000
  x <- func
  xs <- delayedStream microsec func
  return $ x:xs

-- Process SDL events
-- return True if quit event has come
procSDLEvent :: IO Bool
procSDLEvent = do
  ev <- pollEvent
  case ev of
    Quit  -> return True
    KeyDown (Keysym { symKey = ks, symModifiers = km } )
      | ks == SDLK_ESCAPE -> return True
      | ks == SDLK_F4 && (KeyModLeftAlt `elem` km || KeyModRightAlt `elem` km) -> return True
    NoEvent  -> return False
    _    -> procSDLEvent

-- Image resource
type ImageResource = [(ImageType, Surface)]

-- Load image resources
loadImageResource :: [ImageType] -> IO ImageResource
loadImageResource = mapM load
  where
    load imgtype = do
      sur <- loadBMP $ (imagePath ++) $ imageFn imgtype
      setNuki sur
      converted <- displayFormat sur
      freeSurface sur
      return (imgtype, converted)

    setNuki sur = setColorKey sur [SrcColorKey] (Pixel 0) >> return ()    -- Set color key to palet 0

releaseImageResource :: ImageResource -> IO ()
releaseImageResource = mapM_ (\(_, sur) -> freeSurface sur)

getImageSurface :: ImageResource -> ImageType -> Surface
getImageSurface imgres = fromJust . (`lookup` imgres)

putimg :: Surface -> ImageResource -> ImageType -> Int -> Int -> IO ()
putimg sur imgres imgtype x y = do
  blitSurface (getImageSurface imgres imgtype) Nothing sur (Just $ Rect x y 0 0)
  return ()


-- Sound resource
type SoundResource = [(SoundType, Maybe Chunk)]

-- Load sound resources
loadSoundResource :: [SoundType] -> IO SoundResource
loadSoundResource sndtypes = mapM load sndtypes
  where
    load :: SoundType -> IO (SoundType, Maybe Chunk)
    load sndtype = flip catch err $ do
      dat <- loadWAV $ (soundPath ++) $ soundFn sndtype
      return (sndtype, Just dat)
      where
        err = \(_ :: SomeException) -> return (sndtype, Nothing)


-- From fixed point integer to cell coordinate
cellCrd :: Int -> Int
cellCrd x = x `div` (chrSize * one)



-- ========
--data Rect = Rect Int Int Int Int


ishit :: Rect -> Rect -> Bool
ishit (Rect l1 t1 r1 b1) (Rect l2 t2 r2 b2) =
  l1 < r2 && t1 < b2 && l2 < r1 && t2 < b1
