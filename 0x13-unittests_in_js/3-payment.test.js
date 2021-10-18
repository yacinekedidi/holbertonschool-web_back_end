const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  it('The usage of the Utils function is valid', () => {
    const res = sendPaymentRequestToApi(10, 5);
    chai.expect(calculateNumberSpy.calledOnce).to.be.true;
    chai.expect(calculateNumberSpy.calledOnceWithExactly('SUM', 10, 5)).to.be
      .true;
    chai.expect(calculateNumberSpy.returned(15)).to.be.true;
    calculateNumberSpy.restore();
  });
});
