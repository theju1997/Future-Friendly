import { Box, Paper, Toolbar } from "@mui/material"
import { MyTabs } from "../../Components/Tabs/MyTabs"

export const Lessons:React.FC<{}>=()=>{
    return <>
    <Box>
        <Paper elevation={3}>
            <Toolbar><h1>React Topics</h1></Toolbar>
                          <MyTabs/>
                            </Paper>
       </Box>
       </>
}