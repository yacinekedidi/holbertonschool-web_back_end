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
        if (studentGrade.studentId === studentInCity.id)
          grade = studentGrade.grade;
      });
      return { ...studentInCity, grade };
    });
}
