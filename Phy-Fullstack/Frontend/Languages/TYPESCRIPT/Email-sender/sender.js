const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
   service: "gmail",
   auth: {
      user: "thejaswinitr@gmail.com",
      pass: "smimcdagaknkrdps"
   }
});

const mailOptions = {
   from: "thejaswinitr@gmail.com",
   to: "harishraghoji11@gmail.com",
   subject: "Nodemailer Test",
   html: "Test sending Gmail using Node JS"
};

transporter.sendMail(mailOptions, function(error, info){
   if(error){
      console.log(error);
   }else{
      console.log("Email sent: " + info.response);
   }
});