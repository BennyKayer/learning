import HasFormatter from "../interfaces/HasFormatter";

class Payment implements HasFormatter {
  // readonly client: string;
  // private details: string;
  // public amount: number;

  // constructor(c: string, d: string, a: number) {
  //   this.client = c;
  //   this.details = d;
  //   this.amount = a;
  // }

  constructor(
    readonly recipient: string,
    readonly details: string,
    readonly amount: number
  ) {}

  format() {
    return `${this.recipient} is owed $${this.amount} for ${this.details}`;
  }
}
export default Payment;
