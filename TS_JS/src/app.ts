import Invoice from "./classes/Invoice.js";
import Payment from "./classes/Payment.js";
import ListTemplate from "./classes/ListTemplate.js";
import HasFormatter from "./interfaces/HasFormatter";

let docOne: HasFormatter;
let docTwo: HasFormatter;

docOne = new Invoice("yoshi", "web work", 250);
docTwo = new Payment("mario", "plumbing work", 200);

let docs: HasFormatter[] = [];

docs.push(docOne);
docs.push(docTwo);

// console.log(docs);

// Interfaces
interface IsPerson {
  name: string;
  age: number;
  speak(a: string): void;
  spend(a: number): number;
}

const me: IsPerson = {
  name: "Paweł",
  age: 23,
  speak(word: string): void {
    console.log(word);
  },
  spend(amount: number): number {
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

const form = document.querySelector(".new-item-form") as HTMLFormElement;

// inputs
const type = document.querySelector("#type") as HTMLSelectElement;
const toFrom = document.querySelector("#toFrom") as HTMLInputElement;
const details = document.querySelector("#details") as HTMLInputElement;
const amount = document.querySelector("#amount") as HTMLInputElement;

const ul = document.querySelector("ul")!;
const list = new ListTemplate(ul);

form.addEventListener("submit", (e: Event) => {
  e.preventDefault();

  let doc: HasFormatter;
  if (type.value === "invoice") {
    doc = new Invoice(toFrom.value, details.value, amount.valueAsNumber);
  } else {
    doc = new Payment(toFrom.value, details.value, amount.valueAsNumber);
  }

  list.render(doc, type.value, "end");

  // console.log(type.value, toFrom.value, details.value, amount.valueAsNumber);
});
