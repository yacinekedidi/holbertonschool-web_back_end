export default function hasValuesFromArray(set, array) {
  return array.every((elem) => Array.from(set).includes(elem));
}
