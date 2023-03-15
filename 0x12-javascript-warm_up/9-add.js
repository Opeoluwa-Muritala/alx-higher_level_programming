#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
if (argv[2] === undefined || argv[3] === undefined) {
  console.log('NaN');
} else { add(argv[2], argv[3]); }
