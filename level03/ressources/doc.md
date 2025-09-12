1. Ls the home

>> -rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03


we have a file with the -s instead of a -x in the owner column

this means that the program will have flag03 permission no matter the user who launched the program

2. scp the program to decompile in dogbolt : 

https://dogbolt.org/

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

