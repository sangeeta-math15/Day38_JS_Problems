//Reads 5 Random 2 Digit values ,then find their sum and the average

let a = Math.floor(Math.random() * 90 + 10);
let b = Math.floor(Math.random() * 90 + 10);
let c = Math.floor(Math.random() * 90 + 10);
let d = Math.floor(Math.random() * 90 + 10);
let e = Math.floor(Math.random() * 90 + 10);
console.log(a);
console.log(b);
console.log(c);
console.log(d);
console.log(e);
let add = a + b +c +d + e;
let average = (add/5);
console.log("Sum of 5 two digit number is : " +add);
console.log("Average of 5 two digit number is : " +average);