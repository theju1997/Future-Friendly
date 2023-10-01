
// to run my sql in js first we have to connect db by using this code 
// for db connection this is my extra folder
var mysql=require('mysql')
var con=mysql.createConnection({
host:'localhost',
user:'root',
password:''
})
con.connect((err:any)=>{
if(err) throw err;
console.log ('db connected')
})
