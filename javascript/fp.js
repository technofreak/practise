/*
Contains generic functions

Based on Functional Programming Chapter #6 from Eloquent JavaScript
*/

function forEach(array, action) {
	// loops through each element in the array, calling action on it
	for (var i = 0; i < array.length; i++) {
		action(array[i]);
	}
}

function negate(func) {
	// returns a new function that negates the return value of the passed
	return function () {
		return !func.apply(null, arguments);
	};
}

function reduce(combine, base, array) {
	// for each item in array, call combine with base and item and store
	// its result as base to build up
	forEach(array, function (element) {
		base = combine(base, element);
	});
	return base;
}

function count(conditional, array) {
	// count the number of items in array for which conditional returns true
	return reduce(function (tot, element) {
		return tot + (conditional(element) ? 1 : 0);
	}, 0, array);
}

function equals(x) {
	// return a function that can check whether the element passed to it is
	// equal to x
	return function (element) {return x === element;};
}

function countZeros(array) {
	// counts the number of zeros in an array
	return count(equals(0), array);
}