var num = [3, 3, 2, 2, 9, 9, 1, 1];
var uniqueNums = num.reduce(function (acc, current) {
    if (!acc.includes(current)) {
        acc.push(current);
    }
    return acc;
}, []);
console.log(uniqueNums);
