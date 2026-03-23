# JavaScript DOM Manipulation

This project focuses on **manipulating the DOM** using JavaScript. You will learn how to select elements, change their content, style, and handle events.

---

## Table of Contents

- [Overview](#overview)
- [Selecting Elements](#selecting-elements)
- [Modifying Content and Style](#modifying-content-and-style)
- [Handling Events](#handling-events)
- [Making Requests](#making-requests)
- [Good Practices](#good-practices)
- [Resources](#resources)

---

## Overview

The **DOM (Document Object Model)** is a structured representation of the HTML document. JavaScript can interact with the DOM to dynamically change the page content or appearance.

---

## Selecting Elements

You can select elements using:

### By Type (Tag)
```js
document.querySelector("p"); // selects the first <p>
document.querySelectorAll("div"); // selects all <div> elements

# JavaScript DOM Manipulation

This project focuses on **manipulating the DOM** using JavaScript. You will learn how to select elements, change their content, style, and handle events.

---

## Table of Contents

- [Overview](#overview)
- [Selecting Elements](#selecting-elements)
- [Modifying Content and Style](#modifying-content-and-style)
- [Handling Events](#handling-events)
- [Making Requests](#making-requests)
- [Good Practices](#good-practices)
- [Resources](#resources)

---

## Overview

The **DOM (Document Object Model)** is a structured representation of the HTML document. JavaScript can interact with the DOM to dynamically change the page content or appearance.

---

## Selecting Elements

You can select elements using:

### By Type (Tag)
```js
document.querySelector("p"); // selects the first <p>
document.querySelectorAll("div"); // selects all <div> elements
```
```js
const el = document.querySelector("p");
el.textContent = "Hello World!";
```