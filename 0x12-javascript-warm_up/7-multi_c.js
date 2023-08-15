#!/usr/bin/node
const myX = parseInt(process.argv[2]);
if (myX > 0) {
  for (let step = 0; step < myX; step++) {
    console.log('C is fun');
  }
} else if (myX <= 0) {
  // Do nothing
} else {
  console.log('Missing number of occurrences');
}
