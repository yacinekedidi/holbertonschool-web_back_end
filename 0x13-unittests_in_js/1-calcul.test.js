const assert = require('assert')
const calculateNumber = require('./1-calcul')

describe('calculateNumber', () => {
    it('SUM', () => {
        assert.strictEqual(calculateNumber("SUM", 5, 5), 10)
        assert.strictEqual(calculateNumber("SUM", 5.7, 5), 11)
        assert.strictEqual(calculateNumber("SUM", 5, 5.7), 11)
        assert.strictEqual(calculateNumber("SUM", 5.4, 5.7), 11)
        assert.strictEqual(calculateNumber("SUM", 5.7, 5.7), 12)
        assert.strictEqual(calculateNumber("SUM", 5, 5.3), 10)
    })

    it('SUBSTRACT', () => {
        assert.strictEqual(calculateNumber("SUBSTRACT", 5, 5), 0)
        assert.strictEqual(calculateNumber("SUBSTRACT", 5.7, 5), 1)
        assert.strictEqual(calculateNumber("SUBSTRACT", 5, 5.7), -1)
        assert.strictEqual(calculateNumber("SUBSTRACT", 5.4, 5.7), -1)
        assert.strictEqual(calculateNumber("SUBSTRACT", 5.7, 5.7), 0)
        assert.strictEqual(calculateNumber("SUBSTRACT", 5, 5.3), 0)
    })

  it('DIVIDE', () => {
        assert.strictEqual(calculateNumber("DIVIDE", 5, 5), 1)
        assert.strictEqual(calculateNumber("DIVIDE", 5.7, 5), 1.2)
        assert.strictEqual(calculateNumber("DIVIDE", 5, 5.7), 0.8333333333333334)
        assert.strictEqual(calculateNumber("DIVIDE", 5.4, 5.7), 0.8333333333333334)
        assert.strictEqual(calculateNumber("DIVIDE", 5.7, 5.7), 1)
        assert.strictEqual(calculateNumber("DIVIDE", 5, 5.3), 1)
        assert.strictEqual(calculateNumber("DIVIDE", 5, 0), 'Error')

    })
})