# How to start the low level learning

# 1) learn a low level language like c
Make a http server in c. Read man pages and documentations.

# 2)  Learn assembly variants

Take a snippet of c code compile in c
 then objdump -d -Mintel ./while | less
  basic 101 of cpu architecture


# 3)  Reverse Engineering 

How the code affects and take the binary aprats to study the code.

crackmes.com to see challenges on reverse engineering the codes

# 4) Pick up a board to learn and code on that
Writing according to architecture.




# Assembly Language

Assembly is human readable format of machine code

as asem.s -o asem.o
gcc -o asem asem.o -nostdlib --static
./asem

echo $? gives the exit status of last program



