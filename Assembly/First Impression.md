
# how to view machine code

To view compiled files in machine code, you can use tools like `objdump` or `hexdump`. Here's how you can achieve this on Arch Linux:

---

### 1. **Compile Your Source Code**

First, compile your source code into an object file or binary executable using a compiler like `gcc` or `clang`:

```bash
gcc -c your_file.c -o your_file.o
gcc your_file.c -o your_program
```

- `your_file.o`: Object file (intermediate compilation output)
- `your_program`: Executable file

---

### 2. **View Machine Code with `objdump`**

Use the `objdump` tool to disassemble the binary and view the machine code:

#### For Object Files:

```bash
objdump -d your_file.o
```

#### For Executables:

```bash
objdump -d your_program
```

This displays the disassembled machine code and its corresponding assembly instructions.

---

### 3. **View Raw Machine Code with `hexdump`**

If you want to see the raw hexadecimal machine code:

```bash
hexdump -C your_program
```

This shows the binary content of the file in a hexadecimal format.

---

### 4. **Use `readelf` for ELF Details**

To get more details about ELF files (common binary format in Linux):

```bash
readelf -a your_program
```

This provides insights into sections, symbols, and program headers.

---

### 5. **Use `xxd` for Hex and Binary Content**

For a cleaner view of binary content:

```bash
xxd your_program
```

This outputs the file in both hexadecimal and ASCII.

---

### 6. **Using `gdb` for Runtime Inspection**

To inspect machine code dynamically during execution:

```bash
gdb your_program
```

In the `gdb` prompt:

```bash
disassemble main
```

This shows the disassembled machine code of the `main` function.

---

These tools should help you analyze the machine code of your compiled files on Arch Linux!