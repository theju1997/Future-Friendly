
import { Grid } from '@mui/material'
import img from '../Staticimage/t.jpg'
export const About:React.FC<{}>=()=>{

    return<>
    <div  style={{backgroundImage:`url(${img})`,height:'800px',backgroundPosition:'center', backgroundRepeat:'no-repeat',backgroundSize:'cover'}}>
    <h1>Hii Im Thejaswini</h1>
    <div>
        <p><a href="./Thejaswini TR (CV).docx">Resume</a></p>
        <p><a href="https://thejaswinitr.dcms.site/">Personal Website/Blog</a></p>
    </div>
    </div>
    </>

}