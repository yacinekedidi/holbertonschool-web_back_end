const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  const sandbox = sinon.createSandbox();
  let logSpy;
  beforeEach(() => {
    logSpy = sandbox.spy(console, 'log');
  });

  afterEach(() => {
    logSpy.restore();
  });

  it('sendPaymentRequestToAPI with 100, and 20', () => {
    sendPaymentRequestToApi(100, 20);
    chai.expect(logSpy.calledWith('The total is: 120')).to.be.true;
    chai.expect(logSpy.calledOnce).to.be.true;
  });

  it('sendPaymentRequestToAPI with 10, and 10', () => {
    sendPaymentRequestToApi(10, 10);
    chai.expect(logSpy.calledWith('The total is: 20')).to.be.true;
    chai.expect(logSpy.calledOnce).to.be.true;
  });
});
