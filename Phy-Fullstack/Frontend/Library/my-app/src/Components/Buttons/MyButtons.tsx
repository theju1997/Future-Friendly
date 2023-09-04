import Button from "@mui/material/Button"

export const MyButtons:React.FC<{}>=()=>{
    return <>
    <h3>Buttons Example</h3>
    <Button color="secondary">Home</Button>
<Button variant="contained" color="success">About</Button>
<Button variant="outlined" color="error">Introduction</Button>
    </>
}