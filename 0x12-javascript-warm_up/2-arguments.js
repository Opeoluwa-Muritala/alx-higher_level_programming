#!/usr/bin/node
argv = process.argv;
if (argv.length === 2){
console.log("No Argument");
}
else if (argv.length === 3){
console.log("Argument found");
}
else{
console.log("Arguments found");
}
