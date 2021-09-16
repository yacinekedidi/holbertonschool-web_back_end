export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    const isBad = students.some((student) => typeof student !== 'string');
    if (!Array.isArray(students) && isBad) {
      throw TypeError('Students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(val) {
    this._name = val;
  }

  get length() {
    return this._length;
  }

  set length(val) {
    this._length = val;
  }

  get students() {
    return this._students;
  }

  set students(arr) {
    this._students = arr;
  }
}
