import { Outlet } from "react-router-dom";
import { Entrypoint } from "../pages/Entrypoint.page";

export let myEntryPointList={
    path:'/',
    element:<> <Outlet/></>,
    children:[
        {
            path:'entry',
            element:<Entrypoint/>
        }
    ]
}