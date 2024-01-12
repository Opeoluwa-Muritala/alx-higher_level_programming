#!/usr/bin/node
const argv = process.argv.slice(2);
function add(a, b) {
	if (isNaN(a)||isNaN(b)){
		console.log("NaN");
	} else {
		console.log(+a + +b);
	}
}
add(argv[0], argv[1]);
