//primitives=number,string,null,undefined,boolean
//reference= {} () []
//references - when you copy that value, it's real value doesnt get copied rather its reference gets passed, and its called reference value and the one that got copied and has a real value its called primitive
//var a=12;
//var b=a;

//b=b+2;
var a=[1,2,3,4];
var b=a;
b.pop();
console.log(a);
console.log(b);
//both a and b changed because of reference types 
//b is referencing a so any changes made to b directly change in a