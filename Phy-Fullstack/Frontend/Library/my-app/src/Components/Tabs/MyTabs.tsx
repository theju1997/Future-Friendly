import * as React from 'react';
import Tab from '@mui/material/Tab';

import Box from '@mui/material/Box';
import { TabList, TabPanel } from '@mui/lab';
import { TabContext } from '@mui/lab';
import { MyProps } from '../../pages/lessons/Props/Myprops';

import { MyButtons } from '../Buttons/MyButtons';
import { MyRating } from '../Ratings/MyRating';
import { MyAvtar } from '../avtar/MyAvtar';
import { MyFragment } from '../Fragment/MyFragment';
import { MyUseStateHook } from '../Hook/MyUseStateHook';
import { MyUseEffect } from '../Hook/MyUseEffect';
import { TwowaysofCss } from '../2waysofcss/TwowaysofCss';
import { H1 } from '../../pages/lessons/Elements/H1';
export let MyTabs:React.FC<{}>=()=>{
  const [value, setValue] = React.useState ('1');

  const handleChange = (event: React.SyntheticEvent, newValue: string) => {
console.log("newValue",typeof newValue)
    setValue(`${newValue}`);
  };

  return (
    <Box sx={{ width: '100%', typography: 'body1' }}>
      <TabContext value={value}>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <TabList onChange={handleChange} aria-label="lab API tabs example">
            <Tab label="props" value="1" />
            <Tab label="Elemetnts" value="2" />
            <Tab label="mui elements" value="3" />
            <Tab label="fragment" value="4" />
            <Tab label="hookes" value="5" />
            <Tab label="TwowaysofCss" value="6" />
            
          </TabList>
        </Box>
        <TabPanel value="1"><MyProps/></TabPanel>
        <TabPanel value="2"> <H1/> </TabPanel>
        <TabPanel value="3">

<MyButtons/><br></br><br></br>
<MyRating/><br></br><br></br>
<MyAvtar/>
        </TabPanel>

        <TabPanel value="4">
          <MyFragment/>
        </TabPanel>
        <TabPanel value="5">
<h1><center>Hookes</center></h1>
<h3>We have 2 types under Hookes</h3><br></br>
<h2>1)Use State</h2>
<p>Use State will helps to update recent value to updated value</p>
<h4>Example-Count value</h4>
<MyUseStateHook/><br></br><br></br><br></br><br></br>
<h2>2) Use Effect</h2>
<p>use effect is a life cycle method (to understand this concept we are using api file)</p>
<h4>Example</h4>
<MyUseEffect/>
        </TabPanel>
        <TabPanel value="6">
<h1><center>Two ways of Css</center></h1>
<TwowaysofCss></TwowaysofCss>
        </TabPanel>
      
      </TabContext>
    </Box>
  );
}