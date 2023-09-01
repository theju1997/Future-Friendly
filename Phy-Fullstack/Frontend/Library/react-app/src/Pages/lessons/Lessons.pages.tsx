import { Box, Paper, Toolbar } from "@mui/material"
import { MyTabs } from "../../Component/Tabs/MyTabs"


export const Lessons:React.FC<{}>=()=>{
    return <>
    <Box>
        <Paper elevation={3}>
            <Toolbar><h1>This is my react notes with example</h1></Toolbar>
        <MyTabs/>
        </Paper>
        
       </Box>
       </>
}