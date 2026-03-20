# JavaScript README

## Introduction
JavaScript is a high-level, interpreted programming language primarily used to create interactive and dynamic content on websites. It is one of the core technologies of the web, alongside HTML and CSS.

## Features
* Lightweight and interpreted
* Object-oriented and functional programming support
* Event-driven and asynchronous
* Cross-platform (runs in browsers and servers)

## Getting Started

### Prerequisites
* A modern web browser (Chrome, Firefox, Edge)
* A code editor (VS Code, Sublime Text, etc.)

### Running JavaScript

#### In the Browser

You can include JavaScript in an HTML file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Example</title>
</head>
<body>
    <script>
        console.log("Hello, World!");
    </script>
</body>
</html>
```

#### Using Node.js

Install Node.js and run:

```bash
node app.js
```

## Basic Syntax

### Variables
```javascript
let name = "John";
const age = 25;
var isStudent = true;
```

### Data Types

* String
* Number
* Boolean
* Object
* Array
* Undefined
* Null

### Functions
```javascript
function greet(name) {
    return `Hello, ${name}!`;
}
```

### Conditionals
```javascript
if (age > 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}
```

### Loops
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

## DOM Manipulation
JavaScript can interact with HTML elements:

```javascript
document.getElementById("demo").innerText = "Hello!";
```

## Asynchronous JavaScript

### Promises
```javascript
const myPromise = new Promise((resolve, reject) => {
    resolve("Success");
});
```

### Async/Await
```javascript
async function fetchData() {
    const response = await fetch("https://api.example.com");
    const data = await response.json();
    console.log(data);
}
```

## Best Practices
* Use `const` and `let` instead of `var`
* Write clean and readable code
* Use meaningful variable names
* Handle errors properly

