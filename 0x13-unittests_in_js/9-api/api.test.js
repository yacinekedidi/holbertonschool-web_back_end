const chai = require('chai');
const request = require('request');

describe('test suite for basic integration testing 1', () => {
  it('GET /', (done) => {
    request('http://localhost:7865', (err, response, body) => {
      chai.expect(err).to.be.null;
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('test suite for basic integration testing 2', () => {
  it('GET /cart/:id with valid id', (done) => {
    request('http://localhost:7865/cart/12', (err, response, body) => {
      chai.expect(err).to.be.null;
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('GET /cart/:id with invalid id', (done) => {
    request('http://localhost/cart:7865/yo', (err, response, body) => {
      chai.expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
