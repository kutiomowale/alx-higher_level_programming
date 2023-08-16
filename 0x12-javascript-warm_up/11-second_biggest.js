#!/usr/bin/node
const myArgs = process.argv.slice(2);
const len = myArgs.length;
if (len <= 1) {
  console.log('0');
} else {
  for (let step = 0; step < len; step++) {
    myArgs[step] = Number(myArgs[step]);
  }
  myArgs.sort((a, b) => a - b);
  console.log(myArgs[len - 2]);
}
