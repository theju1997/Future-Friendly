
import { Carousel } from 'react-bootstrap'
import img1 from '../../Static/images/1.jpg'
import img2 from '../../Static/images/2.jpg'
import img3 from '../../Static/images/3.jpg'
export const MySlider:React.FC<{}>=()=>{
    return <>
    <Carousel>
      <Carousel.Item>
      <img height='400px' width='100%' src={img1}/>
        <Carousel.Caption>
          <h3>First slide label</h3>
          <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>git 
      <img height='400px' width='100%' src={img2}/>
        <Carousel.Caption>
          <h3>Second slide label</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
      <img height='400px' width='100%' src={img3}/>
        <Carousel.Caption>
          <h3>Third slide label</h3>
          <p>
            Praesent commodo cursus magna, vel scelerisque nisl consectetur.
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel></>
}