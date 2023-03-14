#!/usr/bin/node
args = process.argv;
string = "";

args.forEach((val, index) => {
 if (index == 2){
  for( i = 0; i < val; i++){
    for(j = 0; j < val; j++){
      string += "X"}
    string += "\n"}}
           )
           
console.log(string)
