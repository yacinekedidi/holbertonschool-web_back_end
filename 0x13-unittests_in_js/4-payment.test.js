const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  // Add a stub
  const calculateNumberStub = sinon.stub(Utils, 'calculateNumber');
  //   Add a spy
  const logSpy = sinon.spy(console, 'log');
  it('The usage of the Utils function is valid', () => {
    // always return the same number 10
    calculateNumberStub.returns(10);
    sendPaymentRequestToApi(100, 20);
    chai.expect(calculateNumberStub.calledOnce).to.be.true;
    chai.expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be
      .true;
    chai.expect(calculateNumberStub.returned(10)).to.be.true;
    chai.expect(logSpy.calledWith('The total is: 10')).to.be.true;
    logSpy.restore();
    calculateNumberStub.restore();
  });
});
