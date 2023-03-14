#!/usr/bin/node
argv = process.argv;

argv.forEach((val,index) => {
if (index > 2){
  console.log("Arguments found");
}
else if (index > 1 && index === 2){
  console.log("Argument found");
}
  });
