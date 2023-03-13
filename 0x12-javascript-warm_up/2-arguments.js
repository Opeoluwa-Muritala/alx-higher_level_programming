#!/usr/bin/node
import {argv} from 'node:process';

argv.forEach((val,index) => {
 if (val = 2){
  console.log("Argument found);
}
else if (val >= 3){
  console.log("Arguments found");
}
else if (val < 2){
  console.log("No Argument")
}
  });
