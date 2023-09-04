import { Outlet } from "react-router-dom";
import { Login } from "../pages/Project/Login/Login.page";
import { Register } from "../pages/Project/Register/Register.page";
import { Home } from "../pages/Project/Home/Home.page";

export const allProjectRoutes={
    path:'/project',
    element:<><Outlet/></>,
    children:[
        {
            path:'login',
            element:<Login/>
        },
        {
            path:'register',
            element:<Register/>
        },
        {
            path:'home',
            element:<Home/>
        }
    ]
}