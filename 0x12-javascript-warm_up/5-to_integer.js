#!/usr/bin/node
const argv = process.argv.slice(2);
if (isNaN(argv[0])){
	console.log("Not a number");
} else {
	console.log(argv[0]);
}
