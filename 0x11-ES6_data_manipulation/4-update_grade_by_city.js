export default function updateStudentGradeByCity(
  students = [],
  city = '',
  // eslint-disable-next-line comma-dangle
  newGrades = []
) {
  return students
    .filter((student) => student.location === city)
    .map((studentInCity) => {
      let grade = 'N/A';
      // eslint-disable-next-line array-callback-return
      newGrades.filter((studentGrade) => {
        // eslint-disable-next-line curly
        if (studentGrade.studentId === studentInCity.id)
          // eslint-disable-next-line nonblock-statement-body-position
          grade = studentGrade.grade;
      });
      return { ...studentInCity, grade };
    });
}
