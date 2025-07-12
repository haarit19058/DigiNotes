
# SHA 256

Steps to follow
1) Bits are appended to the original input to make it compatible wiht the hash functions. Total bits must always be 64 short of any multiple of 512. The first bit added is always 1 and the rest are zeroes
2) Length of original message is padded to the result from step 1. Length is expressed in the form of 64 bits. Resultant string will now be a multiple of 512. Used to increase complexity of the function.  
	1) Original MSG + padding bits       +   length of input(last 64 bits)  = The final string that has to be hashed
3) The entire message is broken down into blocks of 512 bits each. 5 buffers are used of 32 bits. They are named A,B,C,D,E . THe first iteration has fixed hexadecimal values.
4) Each 512 bit blocks is broken down to 16 sub blocks of 32 bits each. There are 4 rounds of operatoins each of them utilizing the ancde register the 512 bit block and a constant k\[t]. Each round has 20 iterations total  80 rounds. The constant vlaue id an array of 80 elements with 16 elements being used every round
5) There is non linear formula for each of the register and the register values are changed every round. 


# Advanced Encryption Standard

Advanced Encryption Standard NIST 2001 
symmetric block cipher -- means same key is used to encrypt and decrypt


