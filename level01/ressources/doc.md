1. get user info

"cat /etc/passwd"
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
....
level00:x:2000:2000::/home/user/level00:/bin/bash
level01:x:2001:2001::/home/user/level01:/bin/bash
level02:x:2002:2002::/home/user/level02:/bin/bash
....
flag00:x:3000:3000::/home/flag/flag00:/bin/bash
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
....
flag13:x:3013:3013::/home/flag/flag13:/bin/bash
flag14:x:3014:3014::/home/flag/flag14:/bin/bash
```

format is : 
{username}:{hashedPassword}:{UserID}:{GroupID}:User ID Info (GECOS):{HomePath}:{DefaultShellPath}

GECOS is used to provide comments about the user : Phone number, email, etc

https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/

2. Here we have an encrypted password for flag01 : 
42hDRfypTqqnw

3. Copy passwd file from vm to local machine using scp
"scp -P 4243 level00@localhost:/etc/passwd ."

3. Using john the ripper to decrypt password

password is abcdefg

4. connect to flag01 to launch getflag and get the password for level02