export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') return '';
  const arr = [];
  set.forEach((elem) => {
    if (elem.startsWith(startString)) {
      // eslint-disable-next-line nonblock-statement-body-position
      arr.push(elem.slice(startString.length));
    }
  });
  return arr.join('-');
}
