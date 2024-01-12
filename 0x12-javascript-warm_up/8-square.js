#!/usr/bin/node
const argv = process.argv.slice(2);
if (isNaN(argv[0])) {
	console.log("Missing size");
} else if (argv[0] > 0) {
	i = argv[0]
	while (i > 0) {
		let row = "";
		for (let j = 0 ;j < argv[0]; j++){
			row += "x"
		}
		i--
		console.log(row);
	}
} else {
}
