1. Find files where flag00 is the owner

"find / -user flag00 2>/dev/null"

Returns 2 files

    /usr/sbin/john
    /rofs/usr/sbin/john

both contain the flag cdiiddwpgswtgt

2. The code used here is a ceasar code, where the chars are shifted a fixed number of position

https://www.dcode.fr/chiffre-cesar
🠞15 (🠜11) give a single comprehensible answer : nottoohardhere

3. Connect as user flag00 with this flag

4. launch getflag to retrieve level01 password