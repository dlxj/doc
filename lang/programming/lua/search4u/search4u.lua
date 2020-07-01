

TEXT = 'sympathy'
--TEXT = 'condescend'

-- 获取所有文件名
os.execute("search4u.bat")

require "sorting"

-- 要排序的文件
filename = "a.txt"

-- 按以下关键字串排序
t1 = {
	"voa1500",
	"TIME单挑1000",
	"片挑200",
	"TIME Key Phrases 200",
}
sorting.run(filename, t1)

function fsize (file)
	local current = file:seek() -- get current position
	local size = file:seek("end") -- get file size
	file:seek("set", current) -- restore position
	return size
end
local f = assert(io.open("a.txt", "r"))
local fw = assert(io.open("out.txt", "w"))

function allwords (f)
	local line = f:read("*line") 	-- current line
	local pos = 1 				    -- current position in the line
	return function ()
				while line do
					print(line)
					local s, e = string.find(line, "%w+", pos)
					if s then 	-- found a word?
						pos = e + 1
						return string.sub(line, s, e)
					else
						line = f:read("*line")
						pos = 1
					end
				end
				return nil
		  end
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


--f = io.open("a.txt","r") -- open input file
assert(f)

for line in allrow(f) do
	--print(line)
	local f2 = assert(io.open(line, "r"))
	n = 0
	t = {}

	b = 0
	for s in allrow(f2) do
		if b == 1 then  t[#t+1] = s; b = 0 end
		for m in string.gmatch(s, TEXT) do
			t[#t+1] = s
			n = n + 1
			b = 1
		end
	end
	if n ~= 0 then
		print(line)
		print(TEXT..':'..n)
		for i=1, #t do
			print(t[i])
		end
		print'\n'
		f2:seek("set")
		ss = f2:read("*all")
		fw:write(ss..'---------------------------------------------------------------------------------------------------\n')
	end
end

f:close()
fw:close()


