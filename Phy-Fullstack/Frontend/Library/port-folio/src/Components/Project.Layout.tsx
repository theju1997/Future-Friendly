import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Unstable_Grid2';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));
export const Project:React.FC<{}>=()=> {
  return (
    
    <Box sx={{ flexGrow: 1 }}>
     <center><h1 >List of the Projects</h1></center> 
      <Grid container spacing={2}>
        <Grid xs={4}>
        <a href='https://theju1997.github.io/MyPortfolio/'> <Item>Portfolio in JS</Item></a>
        </Grid>
        <Grid xs={4}>
          <a href='https://theju1997.github.io/Calculator/'> <Item>Dynamic Calculator</Item></a>
         
        </Grid>
        <Grid xs={4} height={100}>
        <a href='https://theju1997.github.io/Future-Friendly/'> <Item>Full stack Notes</Item></a>
        </Grid>
        <Grid xs={4}>
        <a href='file:///D:/Apponix/Future-Friendly/Phy-Fullstack/Frontend/FrameWork/Bootstrap/Flipkart/Flipkart.html'> <Item>FlipKart</Item></a>
        </Grid>
        <Grid xs={4}>
        <a href='http://localhost:3000/entry'> <Item>React Project</Item></a>
        </Grid>
        <Grid xs={4}>
        <a href=''> <Item>Portfolio in React</Item></a>
        </Grid>
        
      </Grid>
    </Box>
  );
}