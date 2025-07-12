# Structures


- A structure is a collection of one or more variables, possibly of different types, grouped together under a single name for convenient handling. (Structures are called ''records'' in some languages, notably Pascal.) Structures help to organize complicated data, particularly in large programs, because they permit a group of related variables to be treated as a unit instead of as separate entities.

```c
struct point { int x; int y; };
```


- A struct declaration defines a type. The right brace that terminates the list of members may be followed by a list of variables, just as for any basic type. That is,  
   struct { ... } x, y, z;             is syntactically analogous to  
   int x, y, z; 
   in the sense that each statement declares x, y and z to be variables of the named type and causes space to be set aside for them.  



## Chatgpt shows how to use the structures

In C programming, structures are user-defined data types that allow you to group together different types of variables under a single name. Each variable within a structure is referred to as a member or field. Structures are used to represent complex data in a more organized and meaningful way.

Here's how you can define and use a structure in C:

### Structure Definition:

You define a structure using the `struct` keyword followed by the structure tag (name) and a list of member variables enclosed in curly braces `{}`.

```c
struct Person {
    char name[50];
    int age;
    float height;
};
```

In this example, we've defined a structure named `Person` with three members: `name`, `age`, and `height`.

### Structure Declaration:

Once you've defined a structure, you can declare variables of that type just like any other data type.

```c
struct Person person1, person2;
```

This declares two variables `person1` and `person2` of type `struct Person`.

### Accessing Structure Members:

You can access structure members using the dot (`.`) operator.

```c
strcpy(person1.name, "John");
person1.age = 25;
person1.height = 5.9;
```

### Using Structures:

Structures allow you to group related data together, which can be useful for organizing and managing data in your programs. For example, you might use structures to represent:

- **Employee Records**: Name, ID, Department, Salary, etc.
- **Student Information**: Name, Roll Number, Marks, Grade, etc.
- **Point Coordinates**: x, y, z coordinates.
- **Complex Numbers**: Real part, Imaginary part.

Here's an example of how you might use a structure to store and display information about a person:

```c
#include <stdio.h>
#include <string.h>

// Define the structure
struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    // Declare a variable of type struct Person
    struct Person person1;

    // Assign values to the members
    strcpy(person1.name, "John");
    person1.age = 25;
    person1.height = 5.9;

    // Display the information
    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);
    printf("Height: %.2f\n", person1.height);

    return 0;
}
```

Output:
```
Name: John
Age: 25
Height: 5.90
```

Structures are a powerful feature of C that allow you to create custom data types tailored to the needs of your program. They provide a way to organize and manage complex data in a clear and structured manner.


## Structures and functions

- The only legal operations on a structure are copying it or assigning to it as a unit, taking its address with &, and accessing its members. Copy and assignment include passing arguments to functions and returning values from functions as well. Structures may not be compared. A structure may be initialized by a list of constant member values; an automatic structure may also be initialized by an assignment.

- The first function, makepoint, will take two integers and return a point structure:  
```c
/* makepoint:  make a point from x and y components */ 
   struct point makepoint(int x, int y) 
   { 
       struct point temp; 
       temp.x = x; 
       temp.y = y; 
       return temp; 
   }
```
    
- Notice that there is no conflict between the argument name and the member with the same name; indeed the re-use of the names stresses the relationship.  makepoint can now be used to initialize any structure dynamically, or to provide structure arguments to a function:  

```c
struct rect screen; 
struct point middle; 
struct point makepoint(int, int); 
screen.pt1 = makepoint(0,0); 
screen.pt2 = makepoint(XMAX, YMAX); 
middle = makepoint((screen.pt1.x + screen.pt2.x)/2, 
				  (screen.pt1.y + screen.pt2.y)/2); 
```



If a large structure is to be passed to a function, it is generally more efficient to pass a pointer than to copy the whole structure. Structure pointers are just like pointers to ordinary variables. The declaration  
   struct point \*pp; 
says that pp is a pointer to a structure of type struct point. If pp points to a point structure, \*pp is the structure, and (\*pp).x and (\*pp).y are the members. To use pp, we might write, for example,  
```c
struct point origin, *pp; 
pp = &origin; 
printf("origin is (%d,%d)\n", (*pp).x, (*pp).y);
```



Pointers to structures are so frequently used that an alternative notation is provided as a shorthand. If p is a pointer to a structure, then p->member-of-structure refers to the particular member. So we could write instead printf("origin is (%d,%d)\n", pp->x, pp->y);


- then these four expressions are equivalent:  
```c
r.pt1.x 
rp->pt1.x 
(r.pt1).x 
(rp->pt1).x 
```
   The structure operators . and ->, together with () for function calls and \[] for subscripts, are at the top of the precedence hierarchy and thus bind very tightly. For example, given the declaration  
   
```c
struct { 
       int len; 
       char *str; 
    } *p; 
```

then  ++p->len increments len, not p, because the implied parenthesization is ++(p->len). Parentheses can be used to alter binding: (++p)->len increments p before accessing len, and (p++)->len increments p afterward. (This last set of parentheses is unnecessary.)  In the same way, \*p->str fetches whatever str points to; \*p->str++ increments str after accessing whatever it points to (just like \*s++); (\*p->str)++ increments whatever str points to; and \*p++->str increments p after accessing whatever str points to.  



## Arrays of structure  \{dictionary kind of structures are posiibles using this concept}


```c
struct key { 
       char *word; 
       int count; 
   } keytab[NKEYS]; 

``` 
declares a structure type key, defines an array keytab of structures of this type, and sets aside storage for them. Each element of the array is a structure. This could also be written  
```c
struct key { 
       char *word; 
       int count; 
   }; 
struct key keytab[NKEYS];
```




 keytab\[] = { 
       "auto", 0, 
       "break", 0, 
       "case", 0, 
       "char", 0, 
       "const", 0, 
       "continue", 0, 
       "default", 0, 
       /* ... \*/ 
       "unsigned", 0, 
       "void", 0, 
       "volatile", 0, 
       "while", 0 
   }; 

The initializers are listed in pairs corresponding to the structure members. It would be more 
precise to enclose the initializers for each "row" or structure in braces, as in  
   { "auto", 0 }, 
   { "break", 0 }, 
   { "case", 0 }, 
   ... 
but inner braces are not necessary when the initializers are simple variables or character strings, and when all are present. 



### Program for counting occurences of all the words 

```c
 #include <stdio.h> 
   #include <ctype.h> 
   #include <string.h> 
   #define MAXWORD 100 
   int getword(char *, int); 
   int binsearch(char *, struct key *, int); 
120 
   /* count C keywords */ 
   main() 
   { 
   } 
       int n; 
       char word[MAXWORD]; 
       while (getword(word, MAXWORD) != EOF) 
           if (isalpha(word[0])) 
               if ((n = binsearch(word, keytab, NKEYS)) >= 0) 
                   keytab[n].count++; 
       for (n = 0; n < NKEYS; n++) 
           if (keytab[n].count > 0) 
               printf("%4d %s\n", 
                   keytab[n].count, keytab[n].word); 
       return 0; 
   /* binsearch:  find word in tab[0]...tab[n-1] */ 
   int binsearch(char *word, struct key tab[], int n) 
   { 
       int cond; 
       int low, high, mid; 
       low = 0; 
       high = n - 1; 
       while (low <= high) { 
           mid = (low+high) / 2; 
           if ((cond = strcmp(word, tab[mid].word)) < 0) 
               high = mid - 1; 
           else if (cond > 0) 
               low = mid + 1; 
           else 
               return mid; 
       } 
       return -1; 
   } 
```

## Self Refrential Structures
- Inside of  a structure pointer to the same kind of structure is passed. 
```c
struct tnode {     /* the tree node: */ 
       char *word;           /* points to the text */ 
       int count;            /* number of occurrences */ 
       struct tnode *left;   /* left child */ 
       struct tnode *right;  /* right child */ 
   }; 
```

#### See the code from the book which is using binary datatype

## Table Lookup

hash tables , Again wll do it later

## Typedef

- C provides a facility called typedef for creating new data type names. For example, the declaration 
```c
typedef int Length;
```

- makes the name Length a synonym for int. The type Length can be used in declarations, casts, etc., in exactly the same ways that the int type can be:
```c
Length len, maxlen; Length *lengths[];
```

It must be emphasized that a typedef declaration does not create a new type in any sense; it merely adds a new name for some existing type.
- But it is possible to make a lot many new data structures using the existing ones in C.


## Unions
A union is a variable that may hold (at different times) objects of different types and sizes, with the compiler keeping track of size and alignment requirements. Unions provide a way to manipulate different kinds of data in a single area of storage, without embedding any machine-dependent information in the program. They are analogous to variant records in pascal.

```c
 union u_tag { 
       int ival; 
       float fval; 
       char *sval; 
   } u;
```


Syntactically, members of a union are accessed as 
union-name.member 
		or 
union-pointer->member



Unions may occur within structures and arrays, and vice versa. The notation for accessing a member of a union in a structure (or vice versa) is identical to that for nested structures. For example, in the structure array defined by  
```c
struct { 
       char *name; 
       int flags; 
       int utype; 
       union { 
           int ival; 
           float fval; 
           char *sval; 
       } u; 
   } symtab[NSYM]; 


// the member ival is referred to as  
   symtab[i].u.ival 
```
   
### explanation by chatgpt

In C programming, a union is a user-defined data type that allows you to store different types of data in the same memory location. Unlike structures, where each member has its own memory location, in a union, all members share the same memory location. This means that a union can only hold one value at a time, but that value can be of any of the specified member types.

Here's the basic syntax for defining a union in C:

```c
union UnionName {
    member1_type member1_name;
    member2_type member2_name;
    // Additional members...
};
```

Where:
- `UnionName` is the name of the union.
- `member1_type`, `member2_type`, etc., are the data types of the union members.
- `member1_name`, `member2_name`, etc., are the names of the union members.

Here's an example of how you might use a union in C:

```c
#include <stdio.h>

union Number {
    int integer;
    float floating_point;
};

int main() {
    union Number num;

    num.integer = 10;
    printf("Integer value: %d\n", num.integer);

    num.floating_point = 3.14;
    printf("Floating point value: %.2f\n", num.floating_point);

    printf("Integer value after assigning floating point: %d\n", num.integer);

    return 0;
}
```

Output:
```
Integer value: 10
Floating point value: 3.14
Integer value after assigning floating point: 1084227584
```

In this example:
- We define a union named `Number` with two members: `integer` of type `int` and `floating_point` of type `float`.
- We declare a variable `num` of type `union Number`.
- We assign a value to `num.integer` and print it.
- We then assign a value to `num.floating_point` and print it.
- When we print `num.integer` again, we see that it has a different value. This is because both `integer` and `floating_point` members share the same memory location, so updating one member will affect the other.

Unions are useful when you need to store different types of data in a compact manner, such as in cases where you want to save memory or when working with data structures that can hold different types of data at different times. However, be careful when accessing union members, as it's easy to inadvertently access the wrong member, leading to unexpected behavior.










## Bit Fields

### Explanation of chatgpt

In C programming, bit fields allow you to specify the size of individual members within a structure in terms of bits rather than bytes. This can be useful for saving memory when storing a set of flags or other data that requires less than a full byte for each member. Bit fields are defined within a structure and provide a way to efficiently utilize memory.

Here's the basic syntax for defining bit fields in C:

```c
struct BitField {
    datatype member1 : width1;
    datatype member2 : width2;
    // Additional members...
};
```

Where:
- `BitField` is the name of the structure.
- `datatype` is the data type of the bit field member.
- `member1`, `member2`, etc., are the names of the bit field members.
- `width1`, `width2`, etc., are the widths of the bit field members in bits.

Here's an example of how you might use bit fields in C:

```c
#include <stdio.h>

struct Flags {
    unsigned int flag1 : 1;
    unsigned int flag2 : 1;
    unsigned int flag3 : 1;
    unsigned int flag4 : 1;
};

int main() {
    struct Flags flags;

    // Set some flags
    flags.flag1 = 1;
    flags.flag3 = 1;

    // Print the values of the flags
    printf("Flag 1: %u\n", flags.flag1);
    printf("Flag 2: %u\n", flags.flag2);
    printf("Flag 3: %u\n", flags.flag3);
    printf("Flag 4: %u\n", flags.flag4);

    // Size of the structure
    printf("Size of struct Flags: %lu bytes\n", sizeof(struct Flags));

    return 0;
}
```

Output:
```
Flag 1: 1
Flag 2: 0
Flag 3: 1
Flag 4: 0
Size of struct Flags: 4 bytes
```

In this example:
- We define a structure `Flags` containing four bit fields (`flag1`, `flag2`, `flag3`, and `flag4`), each occupying 1 bit.
- We set some flags and print their values.
- We also print the size of the structure, which is 4 bytes because the compiler typically aligns bit fields to the nearest byte boundary.

Bit fields are particularly useful for defining and manipulating flags, status bits, or other data where each member represents a single bit of information. However, there are some limitations and considerations when using bit fields, such as compiler-dependent behavior and potential portability issues. Additionally, bit fields are not suitable for performance-critical applications due to potential overhead and limitations on bit manipulation operations.


No, not necessarily. While it's true that bit fields are often defined within structures using integers (usually unsigned), structures in C can contain a variety of data types, not just bit fields. 

Here are a few key points to consider:

1. **Bit Fields**: When you define members within a structure using the `:` syntax to specify the number of bits, you're creating bit fields. These members are indeed represented using integers, typically unsigned, but they're a specific usage of integers within structures.

2. **Regular Members**: Structures can also contain regular members that are not bit fields. These members can have any data type, including integers, floating-point numbers, characters, arrays, pointers, other structures, etc. 

   ```c
   struct Example {
       int regularInt;
       float regularFloat;
       char regularChar;
       // Other regular members...
   };
   ```

3. **Mixing Bit Fields with Regular Members**: You can mix bit fields with regular members within the same structure. This allows you to create structures that contain both bit-level and byte-level data.

   ```c
   struct Mixed {
       unsigned int bitField : 1;
       int regularInt;
       // Other members...
   };
   ```

So, while structures with unsigned int members could potentially contain bit fields, it's not a requirement. The presence of bit fields within a structure is indicated by the `:` syntax used when declaring the members. Regular members within structures can have any data type and are not constrained to being bit fields.









# Topics Remaining to cover from the chapter due to complexities
## typedef
## Union 
## Bit-Fields




# There is a lot more to explore. What I have learnt is jus the intro. Using C to code will make me learn a lot many things.