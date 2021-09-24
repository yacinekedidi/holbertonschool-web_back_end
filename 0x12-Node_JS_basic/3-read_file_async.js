/* eslint-disable comma-dangle */
module.exports = async function countStudents(path) {
  // eslint-disable-next-line global-require
  const fs = require('fs');
  try {
    const data = await fs.promises.readFile(path, { encoding: 'utf8' });

    const students = data.trim('').split('\n').slice(1);
    console.log(`Number of students: ${students.length}`);
    const studentsByField = {};
    students.forEach((student) => {
      const studArr = student.split(',');
      if (!studentsByField[studArr.slice(-1)]) {
        studentsByField[studArr.slice(-1)] = [];
      }

      studentsByField[studArr.slice(-1)].push(studArr[0]);
    });
    Object.keys(studentsByField).forEach(
      (field) =>
        // eslint-disable-next-line implicit-arrow-linebreak
        console.log(
          `Number of students in ${field}: ${
            studentsByField[field].length
          }. List: ${studentsByField[field].join(', ')}`
        )
      // eslint-disable-next-line function-paren-newline
    );
  } catch (err) {
    throw Error('Cannot load the database');
  }
};
