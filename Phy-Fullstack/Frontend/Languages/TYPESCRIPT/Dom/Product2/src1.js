

let div=document.getElementById('root1')
let naturelove=[
    {name:'cutegirl',video:'v1.webm'},
    {name:'gowns',video:'v2.webm'},
    {name:' saree',video:'v3.webm'},
    {name:'chudi ',video:'v4.webm'},
    {name:'dangrees ',video:'v5.webm'},
    {name:'t-shirt ',video:'v6.webm'},
    {name:'hairstyle ',video:'v3.webm'},
    {name:' anklet',video:'v1.webm'},
    {name:'croptop ',video:'v4.webm'},
    {name:' Bangle',video:'v6.webm'},
    {name:'croptop ',video:'v5.webm'},
    {name:' Bangle',video:'v2.webm'},

]
// map function used for the purpose we when we click it will repeat many times 
function displayProducts(){
    naturelove.map((item)=>{
        let video=document.createElement('vid')
        video.src=item.image
        video.style.width="200px",
        video.style.height="200px",
        div.appendChild(video)
    })
}