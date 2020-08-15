
// For all of these, what is the value of a when the function gets called with the alert()
// #1
function q1() {
    var a = 5;
    if(a > 1) {
        a = 3;
    }
    console.log("q1 my bet is 3 ", a);
}

//#2
var a = 0;
function q2() {
    a = 5;
    console.log("q2 my bet is 5 ", a);
}

function q22() {
    console.log("q22 my bet is 0 ",a);
}


//#3
function q3() {
    window.a = "hello";
}


function q32() {
    console.log("q32 my bet is hello ",a);
}

//#4
var a = 1;
function q4() {
    var a = "test";
    console.log("q4 my bet is test",a);
}

//#5
var a = 2;
if (true) {
    var a = 5;
    console.log("q5 my bet is 5",a);
}
q1();
q2();
q22();
q3();
q32();
q4();
console.log("q6 my bet is 2",a);
