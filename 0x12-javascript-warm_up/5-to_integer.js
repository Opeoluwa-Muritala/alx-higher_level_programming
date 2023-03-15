#!/usr/bin/node
argv = process.argv

 
if (argv[2] == undefined || isNaN(argv[2]) == true){
  console.log('Not a number');
}
else {
  console.log(parseInt(argv[2]));
}



