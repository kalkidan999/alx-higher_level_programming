#!/usr/bin/node
let x = 0;
process.argv.forEach((val, index) => {
  x++;
  if (index === 2) {
    console.log(`${val}`);
  }
  if (index === 3) {
    console.log('is');
  }
});
