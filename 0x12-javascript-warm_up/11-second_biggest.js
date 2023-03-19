#!/usr/bin/node
let argv = process.argv;
argv.splice(1, 2);
function secondLargest() {
  let largest = Number.NEGATIVE_INFINITY;
  let secondLargest = Number.NEGATIVE_INFINITY;
  for (let i = 0; i < arguments.length; i++) {
    const num = arguments[i];
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
  return secondLargest !== Number.NEGATIVE_INFINITY ? secondLargest : null;
}
console.log(secondLargest(argv));
