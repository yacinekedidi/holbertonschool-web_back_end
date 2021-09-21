export default function cleanSet(set, startString) {
  const arr = [];
  set.forEach((elem) => {
    if (startString && elem.startsWith(startString)) {
      // eslint-disable-next-line nonblock-statement-body-position
      arr.push(elem.slice(startString.length));
    }
  });
  return arr.join('-');
}
