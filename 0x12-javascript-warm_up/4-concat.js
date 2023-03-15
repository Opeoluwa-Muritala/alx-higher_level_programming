#!/usr/bin/node
const args = process.argv;

if (args.length === 4) {
  let string1 = args[2];
  let string2 = args[3];
} else if (args.length === 3) {
  let string1 = args[2];
  let string2 = undefined;
} else {
  let string1 = undefined;
  let string2 = undefined;
}

const string = string1.concat(' is ', string2);
console.log(string);
