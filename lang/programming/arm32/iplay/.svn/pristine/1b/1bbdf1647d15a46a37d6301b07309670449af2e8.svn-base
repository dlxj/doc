
--[[
DB 1st:
  Generate a sqite database that contain a table, this table has a lots of Inflection Words and it's original form. 
  data source is extra from "Collins Cobuild Advanced Learner's Dictionary of British English.mobi" 
  by use calibre's pluin name as KindleUnpack. you can get a html file, this is all we need.
  note: we have to convert that html file to utf-8 format, i's origianl encoding was "West European Latin Endoding".
DB 2st:
  Generate a sqite database that contain a table, this table has a lots of Words and it's pronunciation audio data(WAV format). 
--]]

--[[
A's, a's
Z's, z's
-ability	-abilities
-an	-ans

attach\E9	attach\E9s
attach\E9 case	attach\E9 cases
--]]

require 'std'

local ffi = require "ffi"
local iplay = ffi.load('./libs/libiplay.so')
ffi.cdef[[
  char* splitter();
  
  char* path_DBWORDWAV();
  char* path_DBINFLECTION();
  char* path_DIRAUDIO();
  char* path_INFLESOURCE();
  
  bool sqIsDbExsit(char *dbname);
  void sqGenSpeakDB();
  void sqGenDBInflectionWords(char *fname,  char *inflection_word, int sizinfle, char *orig_word, int sizorig, bool no_more_data);
  char* sqGetOrigWord(char *dbname, char *inflection_word);
  void speak(char *word);
]]

SPLITTER = lstring(iplay.splitter()) 
DBWORDWAV    = lstring(iplay.path_DBWORDWAV())
DBINFLECTION = lstring(iplay.path_DBINFLECTION())
DIRAUDIO   = lstring(iplay.path_DIRAUDIO())
INFLESOURCE = lstring(iplay.path_INFLESOURCE())

local function GenSpeakDB()
  iplay.sqGenSpeakDB();
end

function speak(word)
  local wd = extraWords(word)
  if (wd ~= nil) then iplay.speak(cbuf(wd)) end
end

function getOrigWord(dbname, infwd)
  return lstring(iplay.sqGetOrigWord(cbuf(dbname), cbuf(infwd)))
end

function putInfwd(dbname, infwd, oriwd, just_colse_db)
  if (just_colse_db) then
    iplay.sqGenDBInflectionWords(cbuf(dbname), nil, -1, nil, -1, true); 
  else
    iplay.sqGenDBInflectionWords(cbuf(dbname), cbuf(infwd), #infwd+1, cbuf(oriwd), #oriwd+1, false);
  end
end

function isDBInflExist(dbname)
  if ( iplay.sqIsDbExsit(cbuf(dbname)) == true ) then return true end
  return false
end

function checkSpace(s)
  if (isSpaceBeggin(s) or isSpaceEnd(s)) then 
    print('ERROR: data not correct!') 
    assert(false) 
  end
end

function genDBInflectionWords(fname, dbname)
  if ( isDBInflExist(dbname) ) then 
    print(string.format([=[db '%s' has been exist.]=], dbname)); 
    assert(false) 
  end
  
  local fr = assert(io.open(fname, "rb"))
  local fw = assert(io.open(fname..'.txt', "wb"))
  local data = fr:read("*all")
  data = data .. [=[<idx:orth value="just4padding">]=]  -- why add this? it's use for doing string match below. 

  local pattern = [=[<idx:orth value="(.-)">(.-)()<idx:orth value=".-">]=]
  local pat = [=[%((<strong>.-</strong>)%)]=]
  local pa  = [=[<strong>(.-)</strong>]=]

  local word = ''; local pos = 1
  repeat
    word, text, pos = string.match (data, pattern, pos)
    if word ~= nil then
      checkSpace(word)  -- ensure that it's not has space charatter at beggin or end
      if ( string.match (word, '^%a+') ~= nil) then  -- must start by letters 
        local w2 = string.match (text, pat)  -- numbers of word's flections that split with a charater ','. 
        if (w2 ~= nil) then
          local t = {}
          for v in string.gmatch (w2, pa) do
            if ( string.find(v, SPLITTER) == nil) then
              checkSpace(v)
              t[#t+1] = v
            else
              local pp = 1
              local ww = ''
              v = v .. ','
              repeat
                ww, pp = string.match(v, '(%a+.-),()', pp)
                if ww ~= nil then
                  checkSpace(ww)
                  t[#t+1] = ww
                end
                until ww == nil
              end
          end
          local seq = table.concat(t, SPLITTER)
          print (word, seq)
          local infwd = seq; local oriwd = word
          putInfwd(dbname, infwd, oriwd, false)
          fw:write (word .. '	' .. seq .. '\r\n')
        end
      end
    end
  until word == nil

  fr:close()
  fw:close()
end

function GenInfleDB()
  if ( isDBInflExist(DBINFLECTION) == false) then 
    genDBInflectionWords(INFLESOURCE, DBINFLECTION)
  end
end

function genDB()
  GenSpeakDB()
  GenInfleDB()
end

function genTest()
  genDB()
  local words = {
    "a", "a's", "ability",
    "war", "dialling codes",
    "Dabrowa Gornicza",
    "field-testing",
    "apple,",
    "?what?"
  }
  for i = 1, #words do
    speak(words[i])
  end
end

--genTest()


