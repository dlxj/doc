-- sorting.lua
-- 输入1：欲排序文件的文件名
-- 输入2：关键字串table，排在前面的优先级高

local io = io
local assert = assert
local pairs = pairs
local ipairs = ipairs
local string = string
local print = print
local table = table
module(...)

-- 去除字串的前后空格
function trim (s)
	return (string.gsub(s, "^%s*(.-)%s*$", "%1"))
end

-- 计算字串的优先级
-- str:字串
-- t: 优先级表
function getlevel(str, t)
	local level = nil
	for i, v in ipairs(t) do
		s = string.find(str,t[i])  -- return: start indx and end indx
		if s then
			level = i
			break
		else
			level = 9999  -- 赋极大值
		end
	end
	return level
end

function allrow(f)
	f:seek("set")
	return function ()
		local line = f:read("*line") 	-- current line
		if line then
			return line
		else
			return nil
		end
	  end
end


function run(filename, t1)

--filename = "a.txt"

-- 按以下字串排序
--[[
t1 = {
	"voa1500",
	"TIME单挑1000",
	"片挑200",
	"TIME Key Phrases 200",
}
--]]

t2 = {}



local f = assert(io.open(filename, "r"))

for line in allrow(f) do
	t2[#t2+1] = line
end

for i in pairs(t2) do
	l = getlevel(t2[i], t1)
	--print(l, t2[i])
end
print('---------------------')

-- 对表进行排序
-- 小的在前面
table.sort(t2, function (a,b)
	l1 = getlevel(a, t1)
	l2 = getlevel(b, t1)
	if l1 == l2 then
		-- level 相同，文件名短的在前面
		if #a == #b then
			return a < b
		else
			return #a < #b
		end
	else
		return l1 < l2
	end
	return l1 < l2
  end)
--for i in pairs(t2) do print(t2[i]) end

f:close()

-- 写文件
local fw = assert(io.open(filename, "w"))
for i=1, #t2 do
	fw:write(t2[i]..'\n')
end

fw:close()

end

