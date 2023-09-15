var mysql=require('mysql')
var con=mysql.createConnection({
    host:'localhost',
    user:'root',
    password:''
    
})
con.connect((err:any)=>{
    if(err)throw err;
    console.log('Db connected')
    con.query("CREATE DATABASE Program",(err:any,res:any)=>{
        if(err)throw err;
        console.log("Db created")
    })
})