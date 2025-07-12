# Types Operators and Expressions


## Datatyeps and sizes

- There are 4 datatypes char, int, float, double
- Qualifiers like short, long, signed,unsigned.

## Constants


## See Types Operators and Constants



## Bit manipulation

Sure! Bit manipulation in C involves performing operations at the individual bit level of integer variables. It can be used for various purposes such as setting, clearing, toggling, or extracting specific bits, as well as performing bitwise logical operations.

Here are some common bitwise operators in C:

1. **Bitwise AND (`&`)**: This operator performs a bitwise AND operation between corresponding bits of two operands. The result is `1` if both bits are `1`, otherwise `0`.

   Example:
   ```c
   int a = 5; // Binary: 101
   int b = 3; // Binary: 011
   int result = a & b; // result is 1 (Binary: 001)
   ```

2. **Bitwise OR (`|`)**: This operator performs a bitwise OR operation between corresponding bits of two operands. The result is `1` if at least one of the bits is `1`, otherwise `0`.

   Example:
   ```c
   int a = 5; // Binary: 101
   int b = 3; // Binary: 011
   int result = a | b; // result is 7 (Binary: 111)
   ```

3. **Bitwise XOR (`^`)**: This operator performs a bitwise XOR (exclusive OR) operation between corresponding bits of two operands. The result is `1` if the bits are different, otherwise `0`.

   Example:
   ```c
   int a = 5; // Binary: 101
   int b = 3; // Binary: 011
   int result = a ^ b; // result is 6 (Binary: 110)
   ```

4. **Bitwise NOT (`~`)**: This operator performs a bitwise NOT (complement) operation on its operand, flipping all bits. 

   Example:
   ```c
   int a = 5; // Binary: 0000 0000 0000 0000 0000 0000 0000 0101
   int result = ~a; // result is -6 (Binary: 1111 1111 1111 1111 1111 1111 1111 1010)
   ```

5. **Bitwise Left Shift (`<<`)**: This operator shifts the bits of its left operand to the left by a number of positions specified by the right operand. 

   Example:
   ```c
   int a = 5; // Binary: 0000 0000 0000 0000 0000 0000 0000 0101
   int result = a << 2; // result is 20 (Binary: 0000 0000 0000 0000 0000 0000 0001 0100)
   ```

6. **Bitwise Right Shift (`>>`)**: This operator shifts the bits of its left operand to the right by a number of positions specified by the right operand. 

   Example:
   ```c
   int a = 20; // Binary: 0000 0000 0000 0000 0000 0000 0001 0100
   int result = a >> 2; // result is 5 (Binary: 0000 0000 0000 0000 0000 0000 0000 0101)
   ```

Bit manipulation is often used in low-level programming, embedded systems, and algorithms where efficiency and control over individual bits are important. It can be used for tasks like setting flags, compressing data, implementing bitwise algorithms, etc.






## Bits code

The function you provided is close to the desired functionality, but it needs a few adjustments to achieve the correct result. Here's the corrected version:

```c
int setbits(int x, int p, int n, int y) {
    int mask = ~(~0 << n); // Create a mask with rightmost n bits set to 1
    int shifted_y = (y & mask) << (p - n + 1); // Extract and shift the rightmost n bits of y
    
    // Clear the bits in x from position p to p - n + 1
    int clear_mask = ~(mask << (p - n + 1));
    x &= clear_mask;

    // OR the shifted_y into x to set the bits
    x |= shifted_y;

    return x;
}
```

Explanation:

1. We create a mask with the rightmost `n` bits set to `1`. This mask will help us extract the rightmost `n` bits from `y`.
2. We extract the rightmost `n` bits from `y` and shift them to align with position `p`.
3. We create a mask to clear the bits in `x` that will be replaced with the bits from `y`.
4. We clear those bits in `x` using the clear mask.
5. We perform a bitwise OR operation between the shifted bits and `x` to set them in `x`.
6. Finally, we return the modified value of `x`.

This function should correctly set the `n` bits of `x` starting from position `p` to the rightmost `n` bits of `y`, leaving the other bits unchanged.

Certainly! Let's use an example to illustrate how the `setbits` function works:

Suppose we have the following inputs:

- `x` = 0b10101101 (binary) = 173 (decimal)
- `y` = 0b1101 (binary) = 13 (decimal)
- `p` = 6
- `n` = 3

We want to set the 3 bits starting at position 6 in `x` to the rightmost 3 bits of `y`.

### Step-by-Step Explanation:

1. **Create a mask to extract the rightmost `n` bits of `y`**:
   - `mask = ~(~0 << n) = ~(~0 << 3) = ~(11111111 << 3) = ~(11111000) = 00000111`

2. **Extract and shift the rightmost `n` bits of `y`**:
   - `shifted_y = (y & mask) << (p - n + 1) = (13 & 00000111) << (6 - 3 + 1) = (00000001) << 4 = 00010000`

3. **Create a mask to clear the bits in `x` from position `p` to `p - n + 1`**:
   - `clear_mask = ~(mask << (p - n + 1)) = ~(00000111 << (6 - 3 + 1)) = ~(00000111 << 4) = ~(11110000) = 00001111`

4. **Clear the bits in `x` using the clear mask**:
   - `x &= clear_mask = 10101101 & 00001111 = 10101101 & 00001111 = 10101101 & 00001111 = 10101101 & 00001111 = 10101101`

5. **Perform a bitwise OR operation between the shifted bits and `x` to set them in `x`**:
   - `x |= shifted_y = 10101101 | 00010000 = 10111101`

### Result:
After applying the `setbits` function with the given inputs, we get:
- `x` = 0b10111101 (binary) = 189 (decimal)

So, `x` has the 3 bits starting at position 6 set to the rightmost 3 bits of `y`, leaving the other bits unchanged.





