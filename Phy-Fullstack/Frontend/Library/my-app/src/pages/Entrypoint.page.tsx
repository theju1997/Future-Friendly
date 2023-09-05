import { Box, Button, Grid, Paper } from "@mui/material"
import { Link } from "react-router-dom"

export const Entrypoint:React.FC<{}>=()=>{
    return <>
    <Box>
        <Paper elevation={3}  >
            
<Grid
  container
  direction="column"
  justifyContent="center"
  alignItems="center"
>
    <Link to="/lessons/lessons">
<Button>lessons</Button></Link>
<Link to='/project/login'>
<Button>Projects</Button>
</Link>
            
</Grid>
        </Paper>
    </Box>
    
    </>
}