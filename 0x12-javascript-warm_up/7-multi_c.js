#!/usr/bin/node
const argv = process.argv.slice(2);
if (isNaN(argv[0])) {
	console.log("Missing number of occurrences");
} else if (argv[0] > 0) {

	while (argv[0] > 0){
		console.log("C is fun");
		argv[0]--;
	}
} else {
}

