export default function createIteratorObject(report) {
  const { allEmployees } = report;
  return Object.values(allEmployees).map((dep) => dep).flat();
}
