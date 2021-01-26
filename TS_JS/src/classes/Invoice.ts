import HasFormatter from "../interfaces/HasFormatter";

class Invoice implements HasFormatter {
  // readonly client: string;
  // private details: string;
  // public amount: number;

  // constructor(c: string, d: string, a: number) {
  //   this.client = c;
  //   this.details = d;
  //   this.amount = a;
  // }

  constructor(
    readonly client: string,
    readonly details: string,
    readonly amount: number
  ) {}

  format() {
    return `${this.client} owes $${this.amount} for ${this.details}`;
  }
}
export default Invoice;
