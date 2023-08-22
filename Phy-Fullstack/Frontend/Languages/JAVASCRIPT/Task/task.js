
   let a = [
  { name: 'person1', cloths: ['pant', 'shirt', 'sleepers'] },
  { name: 'person2', cloths: ['pant', 'shirt'] },
  { name: 'person3', cloths: ['shirt', 'sleepers'] },
  { name: 'person4', cloths: ['sleepers'] }
];

let b = ['sleepers', 'pant','shirt'];

let lists = {};

a.map(item => {
  b.map(cloth => {
    if (item.cloths.includes(cloth)) {
        console.log(" lists[cloth]", lists[cloth])
      lists[cloth] = lists[cloth] || [];
      lists[cloth].push(item);
    }
  });
});


console.log("Lists based on elements in array 'b':",lists);
b.map(cloth => {
  if (lists[cloth]) {
    console.log(`List of People wearing ${cloth}:`);
    console.log(lists[cloth]);
    console.log("------------------");
  }
});

