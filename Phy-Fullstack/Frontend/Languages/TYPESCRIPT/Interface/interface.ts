interface Iflowers{
    name:string,
    color:string,
    praice:number,
    count?:string
}

let flower:Iflowers={name:'Rose',color:'red',praice:20}
console.log(flower)
console.log(flower.praice)
flower.count="many"