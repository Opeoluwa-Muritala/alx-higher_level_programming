#!/usr/bin/node

exports.addMeMaybe = function (num, _function){
	num++;
	return _function(num);
}
