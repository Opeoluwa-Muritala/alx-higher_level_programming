#!/usr/bin/node
args = process.argv;

  if (args.length === 3) {
    string1 = args[2];
  }
  if (args.length === 4) {
    string2 = args[3];
  }


string = string1.concat(' is ', string2);
console.log(string);
