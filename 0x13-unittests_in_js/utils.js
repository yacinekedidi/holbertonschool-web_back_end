const Utils = {
  calculateNumber(type, a, b) {
    const x = Math.round(a);
    const y = Math.round(b);
    switch (type) {
      case 'SUM':
        return x + y;
        break;
      case 'SUBTRACT':
        return x - y;
        break;
      case 'DIVIDE':
        return y ? x / y : 'Error';
        break;
      default:
        break;
    }
  },
};

module.exports = Utils;
