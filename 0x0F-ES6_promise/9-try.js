export default function guardrail(mathFunction) {
  let res;
  try {
    res = mathFunction();
  } catch (err) {
    res = `Error: ${err.message}`;
  }
  return [res, 'Guardrail was processed'];
}
