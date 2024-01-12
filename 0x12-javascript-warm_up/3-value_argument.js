#!/usr/bin/node
const argv = process.argv.slice(2)
if (!argv[0]){
	console.log("No arguement");
} else {
	console.log(argv.join(""));
}
