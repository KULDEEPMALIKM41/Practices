let btn = document.getElementById('btn');
// console.log(btn);
btn.addEventListener('click', func1);
// btn.addEventListener('dblclick', func2);
// btn.addEventListener('mousedown', func3);

function func1(e) {
    console.log("Thanks", e);
    e.preventDefault(); // remove default attribute feature
}

// function func2(e) {
//     console.log("Thanks its a double click", e);
//     e.preventDefault();
// }

// function func3(e) {
//     console.log("Thanks its a mouse down ", e);
//     e.preventDefault();
// }

// 


document.querySelector('body').addEventListener('mousemove', function(e){
    console.log(e.offsetX, e.offsetY);
    document.body.style.backgroundColor = `rgb(${e.offsetX}, ${e.offsetY},${(e.offsetX/2*e.offsetY/2)/2})`;
    console.log('You triggered mouse move event')
})
