const assert = require('assert')
const chai = require("chai")
const calculateNumber = require('./1-calcul')

describe('calculateNumber', () => {
    it('SUM', () => {
        chai.expect(calculateNumber("SUM", 5, 5)).to.equal(10)
        chai.expect(calculateNumber("SUM", 5.7, 5)).to.equal(11)
        chai.expect(calculateNumber("SUM", 5, 5.7)).to.equal(11)
        chai.expect(calculateNumber("SUM", 5.4, 5.7)).to.equal(11)
        chai.expect(calculateNumber("SUM", 5.7, 5.7)).to.equal(12)
        chai.expect(calculateNumber("SUM", 5, 5.3)).to.equal(10)
    })

    it('SUBSTRACT', () => {
        chai.expect(calculateNumber("SUBTRACT", 5, 5)).to.equal(0)
        chai.expect(calculateNumber("SUBTRACT", 5.7, 5)).to.equal(1)
        chai.expect(calculateNumber("SUBTRACT", 5, 5.7)).to.equal(-1)
        chai.expect(calculateNumber("SUBTRACT", 5.4, 5.7)).to.equal(-1)
        chai.expect(calculateNumber("SUBTRACT", 5.7, 5.7)).to.equal(0)
        chai.expect(calculateNumber("SUBTRACT", 5, 5.3)).to.equal(0)
    })

  it('DIVIDE', () => {
        chai.expect(calculateNumber("DIVIDE", 5, 5)).to.equal(1)
        chai.expect(calculateNumber("DIVIDE", 5.7, 5)).to.equal(1.2)
        chai.expect(calculateNumber("DIVIDE", 5, 5.7)).to.equal(0.8333333333333334)
        chai.expect(calculateNumber("DIVIDE", 5.4, 5.7)).to.equal(0.8333333333333334)
        chai.expect(calculateNumber("DIVIDE", 5.7, 5.7)).to.equal(1)
        chai.expect(calculateNumber("DIVIDE", 5, 5.3)).to.equal(1)
        chai.expect(calculateNumber("DIVIDE", 5, 0)).to.equal('Error')
    })
})