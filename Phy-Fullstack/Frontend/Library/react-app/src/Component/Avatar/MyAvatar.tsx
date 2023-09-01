import { Avatar } from "@mui/material"
import img from '../../static/images/1.jpg'
import img1 from '../../static/images/2.jpg'
import img2 from '../../static/images/3.jpg'
export const MyAvtar:React.FC<{}>=()=>{
    return <div>
        <Avatar alt="Remy Sharp" src={img} />
<Avatar alt="Travis Howard" src={img1} />
<Avatar alt="Cindy Baker" src={img2} />
    </div>
}

