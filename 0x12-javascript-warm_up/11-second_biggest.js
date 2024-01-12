#!/usr/bin/node
const argv = process.argv.slice(2);
if (!argv[0]) {
	console.log("0");
} else if (!argv[1]) {
	console.log("0");
} else {
	let large = 0;
	let secondlargest = 0;
	for( let i = 0;i< argv.length; i++){
		if (large < argv[i]) {
			large = argv[i];
		}
	
	for (let j = 0; j < argv.length; j++) {
                        if (large > argv[j] && secondlargest < argv[j]) {
                                secondlargest = argv[j];
                        }
	}
	}
	console.log(secondlargest);
}
