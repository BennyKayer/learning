import sum from "./sum";
import switchClassName from "./class";

var assert = require("assert");
assert.equal(sum(5, 3), 8);
var obj = {
    className: "first bordered"
};

switchClassName(obj, "visible");
console.log(obj.className);
switchClassName(obj, "bordered");
console.log(obj.className);

var buffer = createBuffer();
buffer("Data");
buffer(" aequatione ");
buffer("quotcunque");
console.log(buffer());

var test = new String("bokmål");
console.log(test.erLik("bokmaal"));
console.log(test.erLik("bokmal"));
var test_2 = new String("Å gå");
console.log(test_2.erLik("Aa gaa"));
console.log(test_2.erLik("A ga"));
