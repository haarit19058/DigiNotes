
# NOTE
- some of the initial notes are in intro.txt in webdev folder.


## Creating a component

```jsx
function Title(){
return (
<h1>hello world</h1>
);
}
```

## Rendering a component

```jsx
<Title></Title>
<Title/>
```


- We can return only return only one parent element in jsx
- we can embed into one element like div.

## Basic React code

```jsx
import "./App.css"

  

function Title(){

  return <h1>I am the title</h1>

}


function App() {

  return <Title/>;

}

  

export default App
```


- Convectionally we have to create a new file for each component by its name.
- module.export Title in title.jsx
- import "./component.jsx" inn app.jsx


# Import-Export

- import \<name to be used > from "./filename"
- export default \<component>

Named Exports
- export {name}
- import {name} from "./filename"

app.jsx
```jsx
import "./App.css"

import Title from "./title.jsx"

  

function App() {

  return <Title/>;

}

  

export default App
```

title.jsx
```jsx
function Title(){

    return <h1>Hello world</h1>;

}

  
// Default Export
export default Title;
import Title from "./title.jsx"

//named export
export {Title};
import {Title} from "./Title.jsx"

```

- In summary named exports are useful  when you want to export multiple values and import them with their specific names, while degault exports are handy for exporting a single value and giving it a custom name when importing. The choice is between the two depends on the structure and requirements of your codebase.
- named export used when we want to export multiple componenets from a single file.

# Writing markup iin jsx

Rules for writing markup in jsx
1) Return a single root element
2) Close all the tags
		Tags like img and br and hr should be taken care of.
3) camelCase most of the things
	- Class attribute of tag is replaced by className. 
	- Bcuz class is a reserved keyword in javascript so we cannot use it as attribute.

 - Can refer to official react js documentation.


# React fragment

It lets you group a list of children without addign extra nodes to the DOM.


```jsx
function App(){
	return (
	<>
	<Title/>
	<Title/>
	<Title/>
	</>
	)
}
```

- if we crete a extra div to contain all three titles then it will create a extra divv node in DOM.
- To avoid this we can simply write the empty tag.


# JSX with curly Braces


- When we use curly braces in jsx it opens a window to pure javascript. we use it when we want to add a little JavaScript logic or reference a dynamic property inside that markup.


```jsx
function Title(){
	let name ="haarit"
	return (
	<div>
	<p>2*2={2*2}</p>
	<h1>{name.toUpperCase()}</h1>
	</div>
	)
}
```


# Structuring our components

see product component

# Styling our components

- We divide the styling on the basis of components.
- We give the same name to component file and function as well as the css file.
- give classNmae same as the function name.

```jsx
import "./Product.css";
export default function Product(){
return 
}
```
- see the code


# React Props

- props are the information that you pass to a jsx tag

```jsx
<Product title="phone" price="30k"/>
<Product title="laptop" price="40000"/>

export default function Product({title,price}){
return (
<div className="Product"
<h4>{title}</h4>
<p>{price}</p>
);
}
```

- If we do console.log(props) the it will be printed two times in the console
- becuz in main.js rect.strictmode is used and it is one of its sideeffects.

# Passing arrays to props

```jsx
features={["fast","reliable"]}
features={a:"fast",b:"reliable"}
```

# Rendering Arrays

```jsx
options=[<li>"Hi tech"</li>,<li>"durable"</li>]

list items are printed separately


options = ["Hi-tech","Durable"]

const list= features.map((feature)=><li>{feature}</li>)


using list rather than rendering features directly.

```


# Conditionals

- Adding elements on the basis of some conditions

```jsx
{price >= 10000 ? <p>Discount : 5%</p> : null}

{price >= 10000 && <p>Discount : 5%</p> }
```


# Dynamic  component styling

```jsx
import "./product.css"

  

function Product({title,price=1,features=["Not Available"]}){

    // console.log(props);

    const list=features.map((feature)=><li>{feature}</li>)

    let styles={backgroundColor : "blue"};

    return (

        <div className="Product" style={styles}>

            <h3> {title}</h3>

            <h5>{price}</h5>

            <h5>{list}</h5>

            {price>30000 ? <p>"Discount of 5%"</p> : null}

        </div>

    );

}

export default Product;
```

background-color from css becomes backgroundColor in jsx


conditional
```jsx
import "./product.css"

  

function Product({title,price=1,features=["Not Available"]}){

    // console.log(props);

    const list=features.map((feature)=><li>{feature}</li>)

    let styles={backgroundColor : price>30000 && "blue"};

    return (

        <div className="Product" style={styles}>

            <h3> {title}</h3>

            <h5>{price}</h5>

            <h5>{list}</h5>

            {price>30000 ? <p>"Discount of 5%"</p> : null}

        </div>

    );

}
```



# Handling Click Events in react

```jsx
function dosomething(){
console.log("button was clicked")
}

export default function Button(){
	return(
		<div>
			<button onclick = {dosomething}>Click me!!</button>
		</div>
	)
}
```

# Handling non click event

```jsx
function dosomething(){
console.log("button was clicked")
}

export default function Button(){
	return(
		<div>
			<button onMouseOver = {dosomething}>Click me!!</button>
		</div>
	)
}
```


# Event Objecct 

```jsx
function handleFormSubmit(event){
	event.preventDefault();
	console.log("Form was submitted")
}

export default function Form(){
	return (
		<form onSubmit={handleformsubmit}}>
			<button>Submit</<button>
		</form>
	)
}
```


# States in react
- Props
- Components
- States

The state is a builtin react object that is used to contain data or information about the componnent.  a components can change  over time; wherever it changes, the component re renders.


```jsx
```



# Hooks

Hooks were new addition in react 16.8
They let you use state and other react features without writing  a class.



# Use State 

useState is a react hook that lets you add a variable to your component

```jsx
const [state, setState] = useState(initialState);
```

usestate returns an array with exactly two values 

1. Current state. During the first render, it will match the initial value that yo uhave passed
2. the set function  that lets you update the state to different value and trigger  a render

```jsx
import usestate from "react"
```

```jsx
import { useState } from "react";

  

export default function Counter(){

    let [count,setState] = useState(0);

  

    function increasecount(){

        count += 1;

        setState(count);

        console.log(count);

    }

  
  
  

    return (

        <div>

            <h3>Count = {count}</h3>

            <button onClick={increasecount}>Click me</button>

        </div>

    )

}
```



# Closure

It is a feature in react that has the acess to the outer funcitons variables


# How re render works

all the code inside the function is re render once the setstate method is called.


```jsx
let [count,setState] = useState(0);  
    function increasecount(){
        count += 1;
        setState(count);
        console.log(count);
}
```


the value gets updated at the time of rerendering of the webpage and not at the time when the function is called.




# Callbacks in set state functions

setcount method is asyncronous method. 
new value of variable depends on the value returned by the previous function

```jsx
export default function Counter(){
    let [count,setState] = useState(0);
    function increasecount(){
        setState(count+1);
        setState(count+1);
        setState(count+1);
        setState(count+1);
        console.log(count);
    }
```
Above code will increase the count only by one bcuz the setState method is asyncronous to overcome this we use callbacks 

```jsx
export default function Counter(){
    let [count,setState] = useState(0);
    function increasecount(){
        setState((currCount)=>{
	        return currCount+1
        });
        setState((currCount)=>{
	        return currCount+1
        });
        setState((currCount)=>{
	        return currCount+1
        });
        setState((currCount)=>{
	        return currCount+1
        });
        console.log(count);
    }
```

This code will increase the value four times in single click.


# More about State

re render will happen only when there is some change in the value of setstate

```jsx
export default function Counter(){
    let [count,setState] = useState(0);
    function increasecount(){
        setState(30);
    }
```

This code wil not rerender the page every time click button is clicked


If we have to use any function to pass the initial value in the usestate then pass the function without parenthesis. If you pass the function with parenthesis then the funciton will be executed every time usetate method is triggered

```jsx
function init(){
	//code
}

export default function Counter(){
    let [count,setState] = useState(init);
    // not like useState(init());
    function increasecount(){
        setState(30);
    }
```
## ...premoves

Both of the given code snippets are using the spread operator to create new objects based on the `prevMoves` object, but they differ in how they order the properties in the resulting object. Here is a detailed breakdown:

1. **First Snippet:**
   ```javascript
   return {...prevMoves, yellow: prevMoves.yellow + 1}
   ```
   - This creates a new object that is a copy of `prevMoves`.
   - It then updates the `yellow` property by incrementing its current value by 1.
   - If `yellow` already exists in `prevMoves`, the new `yellow` property (with the incremented value) will overwrite the existing one.
   - The properties in the resulting object will maintain the order from `prevMoves`, with `yellow` being updated (or added if it doesn't exist).

2. **Second Snippet:**
   ```javascript
   return {red: prevMoves.red + 1, ...prevMoves}
   ```
   - This creates a new object starting with a `red` property, which is set to the current value of `prevMoves.red` incremented by 1.
   - It then spreads the `prevMoves` object, copying all its properties into the new object.
   - Since the spread operator (`...prevMoves`) comes after the `red` property definition, if `prevMoves` also contains a `red` property, the value from `prevMoves` will overwrite the incremented value set at the beginning.
   - Essentially, this means that the `red` property in the resulting object will have the same value as `prevMoves.red` (not incremented), since the value from `prevMoves` comes after and overwrites the earlier increment.

### Practical Example

Consider `prevMoves` is defined as:
```javascript
const prevMoves = { red: 2, yellow: 3, blue: 1 };
```

- **First Snippet:**
  ```javascript
  const newMoves = { ...prevMoves, yellow: prevMoves.yellow + 1 };
  ```
  Results in:
  ```javascript
  newMoves = { red: 2, yellow: 4, blue: 1 };
  ```

- **Second Snippet:**
  ```javascript
  const newMoves = { red: prevMoves.red + 1, ...prevMoves };
  ```
  Results in:
  ```javascript
  newMoves = { red: 2, yellow: 3, blue: 1 };
  ```
  Here, `red` is initially set to `3` but then overwritten back to `2` by the spread operation.

### Conclusion

- The first snippet effectively increments the `yellow` count.
- The second snippet attempts to increment the `red` count but gets overwritten, so it doesn't actually increment `red` in the resulting object.

Understanding this difference is crucial when updating state objects in frameworks like React, where immutability and correct property ordering affect state management.



# Arrays and states


- We can use arrays and objects with the state variables.
- If there is cange in existing arrays and objects then react doesnt take them as new objects/arrays so it wont rerender the components.
- To reflect the change we will have to spread the array/objects


# Simple to do list

# Unique Key for list items

 - always use map and filter to deal with array in react js and see the documentation for more info

# Updating in arrays

## Updating all elements
## updating a single element



# Lottery Game


# Functions as props

js functions are first class props

This means that they can be passed to a function as argument, returned to it and assigned to a variable



# forms in react

All the forms in react maintains their internal state.




