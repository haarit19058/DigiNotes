## Creating code from fusion 360 model.
- Go to manufacture
- setup the operation type
- go to stock and setup the size of raw material
- now go to profile roughing
- select the tool
	- select general turning
	- select vnmt tool because it can do most of operation.
- now  export the code to notepad by right clicking on the setup and select post processing.

## Editing and uploading code
- Edit G00X30Z0 value at the starting. Set X according to your raw material.
- from the main code keep the code till G97 and remove the rest.
- paste you code below it.
- change all m3 to m4
- and add G75X0Z0 at the end of the code in place of G53
- add % symbol at the end of the code.

# note : While removing the code we have to remove some part of the newly written code upto G97.

In turning machine go to Program Manager> RSP > Set mode to receive .
Open WINPCIN and upload you code to the machine.
Stop the receive by stop button


## Setup the Machine
- go to NC directory
- renumber the code and excecute
- Take the offset 
- check the offset
	- GO to mdi 
	- G75X0Z0
	- G00X0Z2
	- reset and repeat cycle.


- press auto and reset the cycle.


# Caution : Keep emergency on while working in the machine.