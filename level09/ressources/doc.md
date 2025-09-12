1. ls home

we have a program level09, and a text file token

token : f4kmm6p|=�p�n��DB�Du{��

2. using cat -v to show non-printing characters

token : f4kmm6p|=M-^B^?pM-^BnM-^CM-^BDBM-^CDu{^?M-^LM-^I

3. reverse engineering and testing level09

<< ./level09 aaaaaaa
>> abcdefg

This program loops through the inputed string and adds the index to each characters

4. creation of a python script that translate the token to a list of ascii decimal code, reversing the program logic (substracting the index instead of adding it), and turn the ascii code back into printable characters

5. we get the password for flag09 : f3iji1ju5yuevaus41q1afiuq

6. launch getflag command