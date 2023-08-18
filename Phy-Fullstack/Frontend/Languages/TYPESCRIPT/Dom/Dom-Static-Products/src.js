

let div=document.getElementById('root')
let girlproducts=[
    {name:'cutegirl',image:'./girl.jpg'},
    {name:'gowns',image:'./gown.jpg'},
    {name:' saree',image:'saree.jpg'},
    {name:'chudi ',image:'chudi.jpg'},
    {name:'dangrees ',image:'dungree.webp'},
    {name:'t-shirt ',image:'tshirt.webp'},
    {name:'hairstyle ',image:'hairstyle.jpg'},
    {name:' anklet',image:'anklet.webp'},
    {name:'croptop ',image:'croptop.jpg'},
    {name:' Bangle',image:'bang.jpg'},
    {name:'coset ',image:'coset.jpg'},
    {name:'watch ',image:'watch.avif'},
    {name:' handbag',image:'bag.webp'},
    {name:' sandle',image:'sandle.jpg'},
    {name:' hearing',image:'jumka.jpg'},
    {name:' nailpolish',image:'nail.jpg'},
    {name:' jacket',image:'jack.jpg'},
    {name:' makeup',image:'make.jpg'},

]
function displayProducts(){
    girlproducts.map((item)=>{
        let image=document.createElement('img')
        image.src=item.image
        image.style.width="200px",
        image.style.height="200px",
        div.appendChild(image)
    })
}