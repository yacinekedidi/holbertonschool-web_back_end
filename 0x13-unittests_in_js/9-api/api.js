const app = require('express')();

const PORT = 7865;

app.get('/', (req, res) =>
  res.status(200).send('Welcome to the payment system')
);
app.get('/cart/:id([0-9]+)', (req, res) => {
  const { id } = req.params;
  return res.status(200).send(`Payment methods for cart ${id}`);
});

app.listen(PORT, () => console.log(`API available on localhost port ${PORT}`));
