import { Outlet } from "react-router-dom";

import { H1 } from "../Pages/lessons/Element/H1";
import { Lessons } from "../Pages/lessons/lessons.pages";
import { MyProps } from "../pages/lessons/props/MyProps";

export let MyLessonsList={
    path:'/Lessons',
    element:<> <Outlet/></>,
    children:[
        {
            path:'props',
            element:<MyProps/>
        },
        {
            path:'ele',
            element:<H1/>
        },{
            path:'lesssons',
            element:<Lessons/>
        }
    ]
}