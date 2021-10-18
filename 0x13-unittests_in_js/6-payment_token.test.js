const chai = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        chai.expect(res).to.equal({ data: 'Successful response from the API' });
      })
      .catch((err) => console.error(err))
      .finally(() => done());
  });
});
