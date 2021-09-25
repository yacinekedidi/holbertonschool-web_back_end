const http = require('http');

const port = 1245;
const host = '127.0.0.1';

/* eslint-disable comma-dangle */
async function countStudents(path) {
  // eslint-disable-next-line global-require
  const fs = require('fs');
  try {
    const data = await fs.promises.readFile(path, { encoding: 'utf8' });

    const students = data.trim('').split('\n').slice(1);
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

const [dbPath] = process.argv.slice(-1);
const app = http
  .createServer((req, res) => {
    if (req.url === '/') res.end('Hello Holberton School!');
    if (req.url === '/students') {
      let str = '';
      let nbr = 0;
      countStudents(dbPath).then((studentsByField) => {
        Object.keys(studentsByField).forEach((field) => {
          nbr += studentsByField[field].length;
          str += `Number of students in ${field}: ${
            studentsByField[field].length
          }. List: ${studentsByField[field].join(', ')}\n`;
        });
        res.write('This is the list of our students\n');
        res.write(`Number of students: ${nbr}\n`);
        res.write(str.slice(0, -1));
        res.end();
      });
    }
  })
  .listen(port, host, () => {});

module.exports = app;
