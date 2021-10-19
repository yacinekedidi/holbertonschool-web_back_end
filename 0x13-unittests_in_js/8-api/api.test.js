const chai = require('chai');
const request = require('request');

describe('test suite for basic integration testing', () => {
  it('GET /', (done) => {
    request('http://localhost:7865', (err, response, body) => {
      chai.expect(err).to.be.null;
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
