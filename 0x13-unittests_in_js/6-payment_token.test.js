const chai = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        chai.expect(res.data).to.equal('Successful response from the API');
        done();
      })
      .catch((err) => done(err));
  });
});
