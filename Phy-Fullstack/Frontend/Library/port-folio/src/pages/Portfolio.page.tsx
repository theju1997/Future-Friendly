import { Box, Grid, Paper } from "@mui/material"
import NavBar from "../Components/NavBar"
import { Profile } from "../Components/Profile"
import { Project } from "../Components/Project.Layout"
import Contact from "../Components/Contact"

export const Portfolio:React.FC<{}>=()=>{

return<>

<Box sx={{m:2}}>

<Paper elevation={3} />
<Grid>
    <NavBar/>
</Grid>

<Grid>
<Profile/>
 
</Grid><br/>

 <Grid>
    <Project/>
 </Grid>
 <Grid>
    <Contact/>
 </Grid>

</Box>

</>

}