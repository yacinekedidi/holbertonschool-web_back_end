const app = require('express')();

const PORT = 7865;

app.listen(PORT, () => console.log(`API available on localhost port ${PORT}`));

app.get('/', (req, res) =>
  res.status(200).send('Welcome to the payment system')
);
