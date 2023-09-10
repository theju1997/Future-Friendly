import { Box, Grid, Paper } from "@mui/material"
import img from "../Staticimage/Thejaswini TR.jpg"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faFacebook, faInstagram, faTwitter } from "@fortawesome/free-brands-svg-icons"
export const Profile:React.FC<{}>=()=>{
return<>
<Box >
<Grid>
<Paper elevation={3}>
<img style={{borderRadius:"rounded-circle" , height:"200px",marginLeft:"80px",marginTop:"20px"}} src={img}/>
<h3 style={{marginLeft: '90px'}}>Thejaswini TR</h3>
</Paper>
</Grid>
</Box>


</>
}