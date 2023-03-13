#!/usr/bin/node
import {argv} from 'node:process';

argv.forEach((val,index) => {
 if (index = 2){
  console.log("Argument found);
}
else if (index >= 3){
  console.log("Arguments found");
}
else if (index < 2){
  console.log("No Argument")
}
  });
