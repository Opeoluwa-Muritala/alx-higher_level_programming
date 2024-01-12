#!/usr/bin/node

exports.callMeMoby = function (num, _function ) {
	for (let x = 0; x <= num; x++){
		_function();
	}
}
