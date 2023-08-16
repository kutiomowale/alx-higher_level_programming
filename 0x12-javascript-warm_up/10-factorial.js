#!/usr/bin/node
function factorial (num) {
  if (Number.isNaN(num)) {
    return 1;
  } else if (num == 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(Number(process.argv[2])));
