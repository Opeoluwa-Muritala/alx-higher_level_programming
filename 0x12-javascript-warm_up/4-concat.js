#!/usr/bin/node
args = process.argv;
args.forEach((val, idx) => {
  if (idx === 2) {
    string1 = val;
  }
  if (idx === 3) {
    string2 = val;
  }
});

string = string1.concat(' is ', string2);
