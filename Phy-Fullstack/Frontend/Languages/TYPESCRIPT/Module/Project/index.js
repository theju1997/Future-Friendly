                                           // for calculator action we are using js
let display=document.getElementById
('display');
                                           // here we are targeting the changes in display
let displayValue='';
                                           // display value should be 0 so we used this command
buttons=document.querySelectorAll
('button');
                                           // we need data for all buttons so we used 
                                           // document.query..(from buttons)
                                            // for work buttons
for(item of buttons){ 
    item.addEventListener('click',(e)=>
    {
    buttonText=e.target.innerText;
                                            // after clcking it should move to inner text 
    console.log(buttonText)
                     // for testing we used console
     
if(buttonText=='x'){
    buttonText='*';
    displayValue+=buttonText;
    display.value=displayValue;
}
else if(buttonText=="C")
{
    displayValue='';
    display.value=displayValue;
}

else if(buttonText=="=")
                     {
                         display.value=eval(displayValue)
                         
                     }

 else{
        displayValue+=buttonText;
     display.value=displayValue;
    }

    })
}
