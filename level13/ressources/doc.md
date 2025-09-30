# level13

Here we have a binary only.

When we run it, we see:

    ./level13
    UID 2013 started us but we we expect 4242


When decompiling it on dogbolt, we see that getuid() is ran, and if the returned value is 4242, a code is put through and encoding function.

Copying the function, compiling it, and giving the code as an argument works, but the right solution for proper reverse engineering is assembly.

Run the executable with gdb.

    gdb ./level13

disassemble, go to the cmp instruction after getuid call

    (gdb) disassemble main
    (gdb) break \*0x0804859a
    (gdb) r

Now we can change the value stored in the eax register, which is where, on our architecture, the return value of functions called is stored. The next asm instruction checks this value to see if it is equal to 4242.

    (gdb) set $eax=4242
    (gdb) c
    Continuing.
    your token is 2A31L79asukciNyi8uppkEuSx
    [Inferior 1 (process 3593) exited with code 050]


## source

- [Cracking a simple program with gdb](https://medium.com/@persecure/cracking-a-simple-program-with-gdb-aefa3aeca14c)