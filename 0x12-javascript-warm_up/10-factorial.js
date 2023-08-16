#!/usr/bin/node
function factorial (num) {
  if (Number.isNaN(num)) {
    return 1;
  } else if (num == 0) {
    return 1;
  } else if (num < 0) {
    return;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
