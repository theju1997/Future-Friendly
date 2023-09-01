import { useRoutes } from "react-router-dom";
import { MyLessonsList } from "./lessons.routes";

export default function MyRoutes(){
    return useRoutes([MyLessonsList])
}