#!/usr/bin/node
const argv = process.argv;
string = '';

if (argv[2] === undefined || isNaN(argv[2]) === true){
  console.log('Missing size');
} else if (argv.length === 3) {
  for (let i = 0; i < argv[2]; i++) {
    for (let j = 0; j < argv[2]; j++) {
     string += 'x';
    }
   string += '\n';
  }
} 

console.log(string);
