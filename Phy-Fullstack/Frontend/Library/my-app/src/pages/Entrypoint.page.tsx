import { Box, Button, Grid, Paper } from "@mui/material"
import { scryRenderedComponentsWithType } from "react-dom/test-utils"
import { Link } from "react-router-dom"
import { fileURLToPath } from "url"

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
    
<Link to="/lessons/lesssons"><Button>lessons</Button></Link>
<Link to='/project/login'><Button>Projects</Button>
</Link>
            
</Grid>
        </Paper>
    </Box>
    
    </>
}
// her we connect lessons and project in entry point
// 1)in my tab file have all components
// 2)Lessons.page file have all tab file 
// 3)entry point have all lessons and project