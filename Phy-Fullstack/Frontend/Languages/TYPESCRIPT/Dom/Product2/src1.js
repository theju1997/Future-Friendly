

let div=document.getElementById('root1')
let naturelove=[
    {name:'nature',video:'v1.webm'},
    {name:'nature',video:'./v2.webm'},
    {name:' nature',video:'v3.webm'},
    {name:'nature ',video:'v4.webm'},
    {name:'nature ',video:'v5.webm'},
    {name:'nature ',video:'v6.webm'},
    {name:'nature ',video:'v3.webm'},
    {name:' nature',video:'v1.webm'},
    {name:'nature ',video:'./v4.webm'},
    {name:' nature',video:'v6.webm'},
    {name:'nature ',video:'v5.webm'},
    {name:' nature',video:'v2.webm'},

]
// map function used for the purpose we when we click it will repeat many times 
function displayProducts(){
    naturelove.map((item)=>{
        let video=document.createElement('video')
        video.src=item.video
        video.style.width="200px",
        video.style.height="200px",
        video.controls
        div.appendChild(video)
    })
}