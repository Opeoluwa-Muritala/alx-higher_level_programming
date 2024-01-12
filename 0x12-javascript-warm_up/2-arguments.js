#!/usr/bin/node
const argv = process.argv.slice(2);
if(argv.length === 0) {
	console.log("No arguement");
} else if (argv.length === 1) {
	console.log("Arguement found");
}
else {
	console.log("Arguements found");
}
