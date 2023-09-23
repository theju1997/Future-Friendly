import { About } from "./Components/About"
import Contact from "./Components/Contact"
import { Education } from "./Components/Education"
import { Project } from "./Components/Project.List"
import { Skills } from "./Components/Skills"
import { Portfolio } from "./pages/Portfolio.page"
import {Router,Routes,Route} from 'react-router-dom'

export const App:React.FC<{}>=()=>{
  return <>
<center><h1 style={{color: 'red', backgroundColor: 'white'}}>PORTFOLIO</h1></center>
<Routes>
<Route path="/" element={<Portfolio/>}/>
<Route path="/about" element={<About/>}/>
<Route path="/Skills" element={<Skills/>}/>
<Route path="/Education" element={<Education/>}/>
<Route path="/Project" element={<Project/>}/>
<Route path="/Contact" element={<Contact/>}/>
</Routes>

</>

}

