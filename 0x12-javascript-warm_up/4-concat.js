#!/usr/bin/node
const argv = process.argv.slice(2);
if (!argv[0]){
	console.log("undefined is undefined");
} else {
	console.log(argv[0] ,"is", argv[1]);
}
