#!/usr/bin/node
args = process.argv;

if (args.length === 4) {
  string1 = args[2];
  string2 = args[3];
} else if (args.length === 3) {
  string1 = args[2];
  string2 = undefined;
} else {
	string1 = undefined;
	string2 = undefined;
}

string = string1.concat(' is ', string2);
console.log(string);
