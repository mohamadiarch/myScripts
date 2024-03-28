local filename = "your_filename.txt"  -- Replace with the actual filename

local f, err = io.open(filename, "r")
if not f then
    print("File not found: " .. err)
    return
end

local body = {}
for line in f:lines() do
    local content = ""
    for letter in line:gmatch"." do
        content = content .. letter
    end
    body[#body+1] = content
end

f:close()

local jsonString = require("json").encode(body)
print(jsonString)
