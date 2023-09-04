
// last line we can see props concept
export let MyProps:React.FC<{}>=()=>{
    return <>
        <h1><u>Props</u> </h1>
        <p>It will Transfer the data from one component to another component 
        (means Parent component to Child component)</p>
        <h3>Example:</h3>
       {Check({a:"Bag"})} 
       <Check a={"Puma Brand"}/>
        </> 
}

let Check:React.FC<{a:any}>=(props)=>{
    return <h2>{props.a}</h2>
}