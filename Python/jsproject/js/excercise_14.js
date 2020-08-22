let ul  = document.querySelector("ul.this");
let element = document.createElement('li');

element.innerHTML = '<b>hello i am kuldeep</b>'

// element.innerText = '<b>hello i am kuldeep</b>'

// let text = document.createTextNode('hello i am kuldeep');
// element.appendChild(text);

// Add a class name to the li element
element.className = 'childul';
element.id = 'childul';

ul.appendChild(element);
// console.log(ul);
// console.log(element);



// let elem2 = document.createElement('h3');
// elem2.id = 'elem2';
// elem2.className = 'elem2';
// let text = document.createTextNode('this is a text for elem2');
// elem2.appendChild(text);

// element.replaceWith(elem2);

// let myul = document.getElementById('myul');
// myul.replaceChild(element,document.getElementById('fui'));
// myul.removeChild(document.getElementById('lui'));

// elem2.removeAttribute('id');
// elem2.setAttribute('title','kuldeep');
// console.log(myul);
// console.log(elem2.hasAttribute('href'));
// console.log(elem2);