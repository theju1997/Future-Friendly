import Rating from "@mui/material/Rating"


export const MyRating:React.FC<{}>=()=>{
    return <>
   <h3>Ratings Example</h3>
   <Rating name="half-rating" defaultValue={2.5} precision={0.5} />
<Rating name="half-rating-read" defaultValue={2.5} precision={0.5} readOnly />


    </>

}