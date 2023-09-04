import { Outlet } from "react-router-dom";
import { MyProps } from "../pages/lessons/Props/Myprops";
import { H1 } from "../pages/lessons/Elements/H1";
import { Lessons } from "../pages/lessons/lessons.pages";

export let myLessonsList={
    path:'/lessons',
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