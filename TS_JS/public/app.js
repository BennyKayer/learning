import Invoice from "./classes/Invoice.js";
import Payment from "./classes/Payment.js";
import ListTemplate from "./classes/ListTemplate.js";
let docOne;
let docTwo;
docOne = new Invoice("yoshi", "web work", 250);
docTwo = new Payment("mario", "plumbing work", 200);
let docs = [];
docs.push(docOne);
docs.push(docTwo);
const me = {
    name: "Paweł",
    age: 23,
    speak(word) {
        console.log(word);
    },
    spend(amount) {
        return amount;
    },
};
// const invOne = new Invoice("Roger", "Work on website", 250.0);
// const invTwo = new Invoice("Mario", "Jacking owe", 300.0);
// let invoices: Invoice[] = [];
// invoices.push(invOne);
// invoices.push(invTwo);
// invoices.forEach((inv) => {
//   // console.log(inv.client, inv.details, inv.amount, inv.format());
//   console.log(inv.client, inv.amount, inv.format());
// });
// invOne.client = "Yoshi";
// invTwo.amount = '25820'
// invTwo.amount = 328952.0;
const form = document.querySelector(".new-item-form");
// inputs
const type = document.querySelector("#type");
const toFrom = document.querySelector("#toFrom");
const details = document.querySelector("#details");
const amount = document.querySelector("#amount");
const ul = document.querySelector("ul");
const list = new ListTemplate(ul);
form.addEventListener("submit", (e) => {
    e.preventDefault();
    let doc;
    if (type.value === "invoice") {
        doc = new Invoice(toFrom.value, details.value, amount.valueAsNumber);
    }
    else {
        doc = new Payment(toFrom.value, details.value, amount.valueAsNumber);
    }
    list.render(doc, type.value, "end");
    // console.log(type.value, toFrom.value, details.value, amount.valueAsNumber);
});
