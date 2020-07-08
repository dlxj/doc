-- sorting.lua
-- ����1���������ļ����ļ���
-- ����2���ؼ��ִ�table������ǰ������ȼ���

local io = io
local assert = assert
local pairs = pairs
local ipairs = ipairs
local string = string
local print = print
local table = table
module(...)

-- ȥ���ִ���ǰ��ո�
function trim (s)
	return (string.gsub(s, "^%s*(.-)%s*$", "%1"))
end

-- �����ִ������ȼ�
-- str:�ִ�
-- t: ���ȼ���
function getlevel(str, t)
	local level = nil
	for i, v in ipairs(t) do
		s = string.find(str,t[i])  -- return: start indx and end indx
		if s then
			level = i
			break
		else
			level = 9999  -- ������ֵ
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

-- �������ִ�����
--[[
t1 = {
	"voa1500",
	"TIME����1000",
	"Ƭ��200",
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

-- �Ա��������
-- С����ǰ��
table.sort(t2, function (a,b)
	l1 = getlevel(a, t1)
	l2 = getlevel(b, t1)
	if l1 == l2 then
		-- level ��ͬ���ļ����̵���ǰ��
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

-- д�ļ�
local fw = assert(io.open(filename, "w"))
for i=1, #t2 do
	fw:write(t2[i]..'\n')
end

fw:close()

end

