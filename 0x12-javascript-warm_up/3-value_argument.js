#!/usr/bin/node
import {argv} from 'node:process';

argv.forEach((val, index) => {
  if (index <= 1){
    console.log('No Argument');
    }
  else if (index >=2){
    console.log('${val}');
    }
  });
