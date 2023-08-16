#!/usr/bin/node
const myList = process.argv.slice(2);
if (myList.length <= 1) {
  console.log('0');
} else {
  myList.sort();
  console.log(myList.slice(-2, -1)[0]);
}
