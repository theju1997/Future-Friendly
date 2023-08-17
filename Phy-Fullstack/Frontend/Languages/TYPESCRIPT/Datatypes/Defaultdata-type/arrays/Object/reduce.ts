
const num = [3, 3, 2, 2, 9, 9, 1, 1];
const uniqueNums = num.reduce((acc, current) => {
  if (!acc.includes(current)) {
    acc.push(current);
  }
  return acc;
}, [] as number[]);

console.log(uniqueNums);
