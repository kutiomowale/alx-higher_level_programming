#!/usr/bin/node
const result = parseInt(process.argv[2]);
if (result) {
  console.log(`My number: ${result}`);
} else {
  console.log('Not a number');
}
