#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size > 0) {
  for (let step = 0; step < size; step++) {
    console.log('X'.repeat(size));
  }
} else if (size <= 0) {
  // Do nothing
} else {
  console.log('Missing size');
}
