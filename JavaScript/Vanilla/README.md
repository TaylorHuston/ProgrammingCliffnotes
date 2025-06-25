# Vanilla JavaScript Examples

This directory contains examples of core JavaScript programming concepts without any frameworks or libraries. Files have been organized by topic to make learning easier.

## Running JavaScript Code

JavaScript can be run in several ways:

- **In a web browser**: Open `index.htm` in your browser and use the browser's developer console
- **With Node.js**: Install Node.js and run:  
  `$ node filename.js`
- **In browser console**: Copy and paste code directly into the browser's developer tools console
- **Online editors**: Use online JavaScript playgrounds like CodePen, JSFiddle, or Repl.it

## Directory Contents

### Core Concepts

- **variables.js** - Variable declarations, types, and scoping
- **strings.js** - String manipulation and methods
- **arrays.js** - Array operations and methods
- **math.js** - Mathematical operations and Math object
- **date.js** - Date and time handling
- **flowControl.js** - Conditional statements, loops, and control flow
- **functions.js** - Function definitions, parameters, and usage patterns
- **scope.js** - Variable scope, closures, and context

### Object-Oriented Programming

- **basicObjects.js** - Object creation and basic object manipulation
- **advancedObjects.js** - Advanced object concepts, prototypes, and inheritance

### Input/Output and DOM

- **inputOutput.js** - User input and output methods
- **workingWithDOM.js** - DOM manipulation and event handling
- **index.htm** - HTML file for testing DOM manipulation examples

### Advanced Concepts

- **ajax.js** - Asynchronous JavaScript and XMLHttpRequest
- **json.js** - JSON parsing and manipulation
- **errorHandling.js** - Error handling and debugging techniques
- **timers.js** - setTimeout, setInterval, and timing functions
- **jqstuff.js** - jQuery-related examples (if jQuery is included)

### Supporting Files

- **simple.txt** - Text file for file reading examples
- **_images/** - Directory containing image files for examples

## Development Environment

### Browser Developer Tools

All modern browsers include developer tools with JavaScript consoles:

- **Chrome/Edge**: Press F12 or Ctrl+Shift+I
- **Firefox**: Press F12 or Ctrl+Shift+K
- **Safari**: Enable Developer menu, then press Cmd+Option+C

### Node.js Setup

To run JavaScript outside the browser:

```bash
# Install Node.js (Ubuntu/Debian)
sudo apt-get install nodejs npm

# Verify installation
node --version
npm --version

# Run a JavaScript file
node filename.js
```

### Code Editors

Recommended editors for JavaScript development:

- **VS Code** - Free, with excellent JavaScript support
- **WebStorm** - Full-featured IDE
- **Sublime Text** - Lightweight with plugins
- **Atom** - Hackable text editor

### Browser Compatibility

These examples use modern JavaScript features. For older browser support, consider:

- **Babel** - Transpiles modern JavaScript to older versions
- **Polyfills** - Add missing features to older browsers

## Learning Path

Recommended order for studying these examples:

1. **Start with basics**: variables.js → strings.js → arrays.js
2. **Control flow**: flowControl.js → functions.js → scope.js
3. **Objects**: basicObjects.js → advancedObjects.js
4. **DOM interaction**: workingWithDOM.js → inputOutput.js
5. **Advanced topics**: ajax.js → json.js → errorHandling.js → timers.js

## Testing Your Code

Use the browser console or Node.js to test code snippets:

```javascript
// Example: Test in browser console
console.log("Hello, World!");

// Example: Test array methods
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);
console.log(doubled); // [2, 4, 6, 8, 10]
```
