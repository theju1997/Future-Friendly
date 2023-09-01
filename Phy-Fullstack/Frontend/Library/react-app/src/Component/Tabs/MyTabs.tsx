import * as React from 'react';
import Tab from '@mui/material/Tab';

import Box from '@mui/material/Box';
import { TabContext, TabList, TabPanel } from '@mui/lab';
import { H1 } from '../../Pages/lessons/Element/H1';

import { MyAvtar } from '../Avatar/MyAvatar';
import ColorButtons from '../BasicsButtons/ColorButtons';
import BasicRating from '../Ratings/BasicRating';
import { MyUseStateHook } from '../Hook/MyUseStateHook';
import { MyFragment } from '../Fragment/MyFragment';
import { MyProps } from '../../pages/lessons/props/MyProps';



export let MyTabs:React.FC<{}>=()=>{
  const [value, setValue] = React.useState('1');

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
            <Tab label="mui elemts" value="3" />
            <Tab label="fragment" value="4" />
            <Tab label="hookes" value="5" />

          </TabList>
        </Box>

        <TabPanel value="1">
            <MyProps/>
        </TabPanel>

        <TabPanel value="2">
            <H1/>
        </TabPanel>

        <TabPanel value="3">

                        <ColorButtons/>
                                   <BasicRating/>
                                              <MyAvtar/>
        </TabPanel>

        <TabPanel value="4">
          
          <MyFragment/>

         </TabPanel>

        <TabPanel value="5">
              <h1>hookes</h1>
                   <MyUseStateHook/>
        </TabPanel>
      
      </TabContext>
    </Box>
  );
}