#!/usr/bin/node
argv = process.argv

argv.forEach((val, index) => 
if (index == 2) && isNan(val){
  console.log('My Number : ${val})}
else {
  console.log('Not a number');
}



