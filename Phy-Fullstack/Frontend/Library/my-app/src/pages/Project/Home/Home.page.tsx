import { Col, Container, Row } from "react-bootstrap"
import { MyBootstrapNavbar } from "../../../Components/Navbar/MyBootstrapNavbar"
import { MySlider } from "../../../Components/slider/MySlider"
import { MyMuiCard } from "../../../Components/Cards/MyMuiCard"
import img from '../../../Static/images/1.jpg'
import img1 from '../../../Static/images/2.jpg'
import img2 from '../../../Static/images/3.jpg'
import { useEffect, useState } from "react"
import { flipkartApi } from "../../../Service/flipkart.service"
export const Home:React.FC<{}>=()=>{
    let [apiData,setApiData]=useState([])
    useEffect(()=>{
        (async()=>{
         let data= await  flipkartApi()
         setApiData(data)
        })()
    },[])
    console.log("apiData",apiData)

    return <>
    <Container fluid>
        <Row>
            <Col>
            <MyBootstrapNavbar/>
            </Col>
        </Row>
        <br />
        <Row>
            <Col>
            <MySlider/>
            </Col>
        </Row>
        <br />
        <h1>Here we used API Way to Display</h1>
        <Row>
        {apiData.map((item:any)=>{return <Col><MyMuiCard img={item.image}/></Col>})}
        </Row>
        <br />
        <h1>Here we used Normal Way to Display</h1>
        <Row>
            <Col>
            <MyMuiCard img={img}/>
            </Col>
            <Col>
            <MyMuiCard img={img1}/>
            </Col>
            <Col>
            <MyMuiCard img={img2}/>
            </Col>
            <Col>
            <MyMuiCard img={img}/>
            </Col>
        </Row>
    </Container>
    
    </>
}