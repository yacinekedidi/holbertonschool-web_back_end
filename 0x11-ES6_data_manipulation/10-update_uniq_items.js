export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');
  map.forEach((v, k, m) => {
    if (v === 1) m.set(k, 100);
  });
  return map;
}
