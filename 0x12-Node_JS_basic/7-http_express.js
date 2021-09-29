const express = require('express');

const port = 1245;
const app = express();
const [dbPath] = process.argv.slice(-1);
/* eslint-disable comma-dangle */
async function countStudents(path) {
  // eslint-disable-next-line global-require
  const fs = require('fs');
  try {
    const data = await fs.promises.readFile(path, { encoding: 'utf8' });

    const students = data.trim().split('\n').slice(1);
    const studentsByField = {};
    students.forEach((student) => {
      const studArr = student.split(',');
      if (!studentsByField[studArr.slice(-1)]) {
        studentsByField[studArr.slice(-1)] = [];
      }

      studentsByField[studArr.slice(-1)].push(studArr[0]);
    });

    return studentsByField;
  } catch (err) {
    throw Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.end('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  let str = '';
  let nbr = 0;
  countStudents(dbPath)
    .then((studentsByField) => {
      Object.keys(studentsByField).forEach((field) => {
        nbr += studentsByField[field].length;
        str += `Number of students in ${field}: ${
          studentsByField[field].length
        }. List: ${studentsByField[field].join(', ')}\n`;
      });
      res.end(
        `This is the list of our students\nNumber of students: ${nbr}\n${str.slice(
          0,
          -1
        )}`
      );
    })
    .catch((err) => {
      res.end(`This is the list of our students\n${err.message}`);
    });
});

app.listen(port, () => {
  console.log(`listening on port ${port}`);
});

module.exports = app;
