import './style.css'
export const TwowaysofCss:React.FC<{}>=()=>{
    let mystyle={width:'200px',height:'200px',backgroundColor:'yellow'}
    return <>
    <div className="mydiv1">First way of Css</div><br /><br/>
    <div style={mystyle}>Another way of Css</div>
    </>
}