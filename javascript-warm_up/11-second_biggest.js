#!/usr/bin/env node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const uniqueArgs = [...new Set(args)].sort((a, b) => b - a);
  if (uniqueArgs.length <= 1) {
    console.log(0);
  } else {
    console.log(uniqueArgs[1]);
  }
}
