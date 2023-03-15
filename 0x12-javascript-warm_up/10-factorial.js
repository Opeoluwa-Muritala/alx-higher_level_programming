#!/usr/bin/node
const argv = process.argv;

function factorial (n) {
  if (n === undefined) {
    return 1;
  }

  if (n === 1 || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(argv[2])));
