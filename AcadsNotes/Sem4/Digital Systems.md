# What Is FPGA
FPGA stands for **Field-Programmable Gate Array**, which is a type of integrated circuit (IC) that can be configured and reprogrammed by the user after manufacturing. Unlike traditional application-specific integrated circuits (ASICs), which are custom-built for specific tasks, FPGAs are versatile and can adapt to a wide range of applications.

### Key Characteristics of FPGAs:

1. **Programmable Logic Blocks**: FPGAs consist of a matrix of configurable logic blocks (CLBs) that can be programmed to perform complex logic operations.
2. **Interconnects**: The logic blocks are connected via programmable interconnects, allowing designers to route signals in a custom manner.
3. **I/O Blocks**: FPGAs include input/output blocks for interfacing with external devices.

### How FPGAs Work:

- **Hardware Description Languages (HDLs)**: FPGAs are programmed using HDLs like VHDL or Verilog, which define the circuit's functionality.
- **Configuration**: Once programmed, the FPGA's internal circuitry is configured to implement the desired digital circuit or system.

### Applications of FPGAs:

1. **Prototyping and Development**: Ideal for testing designs before creating ASICs.
2. **Signal Processing**: Widely used in high-speed signal processing tasks like image processing and audio processing.
3. **Communication Systems**: Deployed in wireless base stations, network routers, and data centers.
4. **Embedded Systems**: Used in automotive, aerospace, and industrial control systems.
5. **AI and Machine Learning**: Increasingly employed for accelerating AI/ML workloads due to their parallel processing capabilities.

### Advantages of FPGAs:

1. **Flexibility**: Can be reprogrammed to meet changing requirements.
2. **Parallelism**: Supports parallel execution, making them suitable for high-speed applications.
3. **Rapid Prototyping**: Allows designers to test and iterate quickly.
4. **Low NRE Costs**: No non-recurring engineering (NRE) costs compared to ASICs, making them economical for small-volume applications.

### Limitations of FPGAs:

1. **Higher Cost per Unit**: More expensive than ASICs for high-volume production.
2. **Power Consumption**: Typically higher than ASICs for the same functionality.
3. **Design Complexity**: Requires expertise in HDLs and hardware design.


## Basics of FPGA



# Lab1

Here’s an explanation of your code, line by line:

---

### Design File (`firstModuleDesign`)

```vhdl
module firstModuleDesign(
    input A, B,  // Declare two input signals: A and B
    output F     // Declare one output signal: F
    );
```

- **`module firstModuleDesign`:** Defines the module named `firstModuleDesign`.
- **`input A, B`:** Declares the input signals `A` and `B`. These are the inputs to the module.
- **`output F`:** Declares the output signal `F`. This is the result of the module's logic.

```vhdl
    assign F = A & B; 
endmodule
```

- **`assign F = A & B`:** Implements the logic for the module. It assigns the logical AND (`&`) of `A` and `B` to the output `F`.
- **`endmodule`:** Marks the end of the module definition.

---

### Testbench File (`first_module_TB`)

```vhdl
module first_module_TB();
```

- **`module first_module_TB`:** Defines a testbench module named `first_module_TB`. A testbench is used to simulate and test the behavior of the design module.

```vhdl
    reg x1, x2;
    wire f;
```

- **`reg x1, x2`:** Declares `x1` and `x2` as `reg` types. In Verilog testbenches, `reg` is used for variables that will be assigned values in procedural blocks like `initial` or `always`.
- **`wire f`:** Declares `f` as a `wire`. Wires are used to represent connections between components and cannot hold values.

```vhdl
    first_module uut(
        .x1(x1),
        .x2(x2),
        .f(f)
    );
```

- **`first_module`:** Instantiates the `firstModuleDesign` module for testing. The instance is named `uut` (Unit Under Test).
- **`.x1(x1)`, `.x2(x2)`, `.f(f)`:** Maps the ports of the `firstModuleDesign` module to the corresponding testbench signals:
    - Input `x1` in the testbench is connected to `A` in the design.
    - Input `x2` in the testbench is connected to `B` in the design.
    - Output `f` in the testbench is connected to `F` in the design.

```vhdl
    initial begin
    x1 = 0; x2 = 0; #10; //delay
    x1 = 0; x2 = 1; #10;
    x1 = 1; x2 = 0; #10;
    x1 = 1; x2 = 1; #10;
    end
endmodule
```

- **`initial begin ... end`:** Defines an `initial` block that runs once at the start of the simulation.
- **`x1 = 0; x2 = 0; #10;`:** Sets `x1` and `x2` to 0, waits for 10 time units (`#10`), and then proceeds to the next line.
- **Subsequent lines:** Similar to the first line, but with different values for `x1` and `x2`, testing all possible combinations of `x1` and `x2`.
    - `(0, 0)`
    - `(0, 1)`
    - `(1, 0)`
    - `(1, 1)`
- **`endmodule`:** Marks the end of the testbench module.

---

### Key Points:

1. **Design Module:** Implements the core logic (`F = A & B`).
2. **Testbench Module:** Simulates the design by applying different input combinations (`x1` and `x2`) and observing the output (`f`).
3. **Simulation Workflow:**
    - Inputs `x1` and `x2` are set to different combinations.
    - The output `f` is observed to verify the correctness of the logic.

	This setup will simulate the `AND` operation and ensure that the design behaves as expected. 


## timescale

The `\`timescale` directive in Verilog is used to specify the **time unit** and **time precision** for simulation. It tells the simulator how to interpret time delays and the granularity of time steps during simulation.

---

### Syntax:

```verilog
`timescale <time_unit> / <time_precision>
```

- **`time_unit`**: Specifies the time measurement unit for delays in the module.
- **`time_precision`**: Defines the smallest time step the simulator will use for calculations.

---

### Explanation of `timescale 1ns / 1ps`:

1. **`1ns` (Time Unit)**:
    
    - All time-related values in the module (e.g., `#10`, `#5`) are interpreted as nanoseconds.
    - For example, `#10` means a delay of **10 nanoseconds**.
2. **`1ps` (Time Precision)**:
    
    - The smallest step of time that the simulator will recognize is **1 picosecond**.
    - This ensures that time delays are accurate to the level of picoseconds, even if the specified delay is in nanoseconds.

---

### Practical Example:

```verilog
`timescale 1ns / 1ps

module example;
    reg a;
    initial begin
        a = 0;      // Time = 0 ns
        #5 a = 1;   // Time = 5 ns
        #2 a = 0;   // Time = 7 ns
    end
endmodule
```

- Here:
    - **Time Unit (`1ns`)** means delays like `#5` are interpreted as 5 nanoseconds.
    - **Time Precision (`1ps`)** ensures that the simulator can handle delays as small as 1 picosecond.

---

### Why Is It Important?

1. **Consistency in Simulation**:
    - All delays and timing in the module are scaled to the same unit, avoiding ambiguity.
2. **Precision Control**:
    - The time precision affects how accurately delays and waveforms are represented in the simulation.
3. **Simulation Granularity**:
    - Choosing an appropriate precision avoids unnecessary computational overhead (e.g., using `1fs` precision for a circuit that doesn't require femtosecond accuracy).

---

### Common `timescale` Settings:

- `1ns / 1ps`: Often used in designs operating at nanosecond scale with picosecond precision.
- `10ns / 1ns`: Used for slower designs where nanosecond precision suffices.
- `1ps / 1fs`: Used for extremely high-speed designs requiring very fine precision.

---

### Notes:

- The `\`timescale` directive is **not synthesizable**—it is only relevant for simulation.
- If omitted, the simulator may default to a specific time scale (often `1ns / 1ns`), which could lead to unintended results if not explicitly defined.



# Verilog Codes

## Structural Codes
 - using logic gates and gate level design

```verilog

`timescale 1ns/10ps
module mux2(A, B, SEL, OUT);
input A, B, SEL;
output OUT;
and (g, A, SEL);
and (f, B, ~SEL);
or (OUT, g, f);
endmodule
```

## Behavioural Code

### Assignment statements
```verilog
module mux2(x1, x2, sel, f);
input x1, x2, sel;
output f;
assign f = (x1 & sel) | (~sel & x2);
endmodule
```

### Procedural Statemetns (similar to cpp coding)

``` verilog
module mux2(x1, x2, sel, f);
input x1, x2, sel;
output reg f;
Sensitivity list
always @(x1, x2, sel)
begin
if (sel == 1 )
f = x1;
else
f = x2;
end
endmodule
```


When to use reg and when not to ??

Testbench   inputs are reg and outputs are wires
Module  inputs are wires and outputs reg

means that when the inputs 


### Always block

always @(\*)  means that it listens for change in any of the inputs
always @(a,b,c) means that it listens for change in any of the three mentioned inputs

always @(posedge clk) means that it listens fo r the positive edge in the clk variable

### for loops

for(integer i = 0;i<16;i = i+1)begin
	useful to give inputs in testbench
		but not allowed by the iee format see why and what can be the alternatives
end


### Trying to familiarize myself with the computer framework to make the notes
it is good for me to get used to keyboard typings and write in english as musch as i vcan do . Practice make the men perfect

first things first i am say all words in my head i am fired and tired of the things teh way the things have been ohhh oh   i was broken from the young age an d taken to the masses taken my message to the plains you make me up you mmade me upa believer pain i let the b m ylife my lve= y comes from pain beleiver thid things third and the sirit to my head off f f f fl i was chokin fromt eh clown falling the ases fralways block make the most beautiful assumptions that not a human can believer pain the let the body dry let the sky rain make a beleiver pain last things last by the grace of the fires and blood in my veins ohh ohh they never did neveer leaved ohh pain ohh 



# Questions

- How many bits do you need to represent +16 to -16 ?? 5
- Name the universal gates --- nand and nor
- Can you implement a full adder using a decoder ?? 

## Write truth table of a full subtractor
### **Full Subtractor**

A **full subtractor** is a combinational circuit that performs subtraction of three bits: two significant bits and a borrow bit. It has three inputs and two outputs:

- **Inputs:**
    - AA: Minuend (the bit being subtracted from)
    - BB: Subtrahend (the bit being subtracted)
    - BinBin: Borrow input (borrow from the previous bit)
- **Outputs:**
    - **Difference** (DD): The result of the subtraction.
    - **Borrow** (BoutBout): The borrow bit, which is passed to the next bit for subtraction.

The full subtractor outputs the difference of the bits and also indicates if a borrow is required for the next subtraction operation.

### **Full Subtractor Logic Equations**

1. **Difference**:
    
    D=A⊕B⊕BinD = A \oplus B \oplus Bin
    
    Where ⊕\oplus represents the XOR operation.
    
2. **Borrow Output**:
    
    Bout=A‾⋅B+(B⊕A)⋅BinBout = \overline{A} \cdot B + (B \oplus A) \cdot Bin
    
    This represents the condition for a borrow: either AA is smaller than BB, or there is a borrow input causing an additional borrow.
    

### **Full Subtractor Truth Table**

|AA|BB|BinBin|DD (Difference)|BoutBout (Borrow)|
|:-:|:-:|:-:|:-:|:-:|
|0|0|0|0|0|
|0|0|1|1|1|
|0|1|0|1|1|
|0|1|1|0|1|
|1|0|0|1|0|
|1|0|1|0|0|
|1|1|0|0|0|
|1|1|1|1|0|

### **Explanation of the Truth Table:**

- When A=0,B=0A = 0, B = 0, and Bin=0Bin = 0, the result of the subtraction is 0, and no borrow is generated.
- In cases where the subtraction cannot be performed without borrowing (e.g., A=0,B=1A = 0, B = 1), a borrow is generated (output Bout=1Bout = 1).
- The **Difference** is the result of the subtraction, and the **Borrow** indicates if the next bit requires a borrow due to the subtraction operation.



# Hazards

There are two adjacent but non intersecting minterms for the outputs o, highlighted by blue and tan shading. For a product of sums logic the function any two adjacent zeros that re covered by a shared minterm can result in a static 0 hazard.


To remove the static hazard joint these two portions or add a minterm that join these two poritons.


## Using this logic we can identify all the hazard in the circuit 

First make the karnaugh map of minterms in the ouput funciton and find teh composnents that are adjacent but not connected. The transition of input at these points is responsible for hazards. To remove the hazard add a new term that corresponds to these area.  For proper explanatoin check teh website.






