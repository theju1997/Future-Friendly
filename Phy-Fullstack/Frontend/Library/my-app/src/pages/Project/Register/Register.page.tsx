import { Box, Button, Grid, Paper, TextField, Toolbar } from "@mui/material"
import { useState } from "react"
import { Link } from "react-router-dom"

export const Register:React.FC<{}>=()=>{
    let [nameVal,setNameVal]= useState('')
   let [emailVal,setEmailVal]= useState('')
   let [passwordVal,setPasswordVal]= useState('')
    return <>
    <Box style={{ height: '100vh'}}>
        <Paper>

        
        <Toolbar/>
        <Grid container spacing={2}>
            <Grid xs={2}></Grid>
            <Grid xs={8}>
                <Paper elevation={3}>
                <Grid
        container
        direction="column"
        justifyContent="center"
        alignItems="center">
            <h1>Register form</h1>
            <TextField value={nameVal}
            id="outlined-basic"
             label="name" 
             variant="outlined"
             onChange={(e)=>{
                setNameVal(e.target.value)
                console.log(e.target.value)}}
              />
            <br />
            <TextField value={emailVal}
            id="outlined-basic"
             label="email" 
             variant="outlined"
             onChange={(e)=>{
                setEmailVal(e.target.value)
                console.log(e.target.value)}}
              />
            <br />
            <TextField
            value={passwordVal}
             id="outlined-basic"
              label="password" 
              variant="outlined"
              onChange={(e)=>{setPasswordVal(e.target.value)}}
               type="password"/>
            <br />
            <Button 
            onClick={()=>{
                alert(`${nameVal}----${emailVal}---${passwordVal}`)
            }}
            variant="contained"
             color='info'>Register</Button>
             <Link to='/project/login'>
             <Button>login</Button>
             </Link>
        </Grid>
                </Paper>
            </Grid>
            <Grid xs={2}></Grid>
        </Grid>
       
        <Toolbar/>
        </Paper>
    </Box>
    
    </>
}