
local ffi = require "ffi"

function LOG(msg)
  print (msg)
end

function DBLOG(patern, ...)
  LOG(string.format(patern, ...))
end

function ERR(msg)
  LOG(msg)
  assert(false)
end

function DBERR(patern, ...)
  DBLOG(patern, ...)
  assert(false)
end

function cbuf(lstring_) 
  if (lstring_ == nil ) then return nil end
  assert( #lstring_ ~= 0 )
  local _cbuf = ffi.new('char[?]', #lstring_ + 1, lstring_)
  return _cbuf
end

function lstring(cbuf_)
  if (cbuf_ == nil) then return nil end
  local _lstring = ffi.string(cbuf_)
  return _lstring
end

-- if a string has one or more space charater at the beggin then return true, otherwise return false 
function isSpaceBeggin(s)
  local pat = '^%s'
  return string.match(s, pat) ~= nil
end
-- if a string has one or more space charater at the end then return true, otherwise return false 
function isSpaceEnd(s)
  local pat = '%s$'
  return string.match(s, pat) ~= nil
end
-- remove a string's space charater that in beggin or in end of it
function trim(s)
  local pat = '^%s*(.-)%s*$';
  return string.match(s, pat)
end

function extraWords(s)
  local pat
  if (s == nil or #s == 0) then DBERR('ERROR: bad argument. in function extraWords()') end
  if (#s == 1) then
    pat = '%a+'
  else
    pat = '%a+.*%a$*'
  end
  return string.match(s, pat)
end




