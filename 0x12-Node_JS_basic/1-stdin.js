const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question(
  'Welcome to Holberton School, what is your name?\n',
  (name) => {
    console.log(`Your name is: ${name}`);
    readline.close();
    console.log('This important software is now closing');
    // eslint-disable-next-line comma-dangle
  }
);
