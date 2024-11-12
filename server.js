const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'sh4d0w.h0g.22@gmail.com',
        pass: '&#*7Z^p$uk2f'
    }
});

app.post('/send_email', (req, res) => {
    const { name, email, message } = req.body;

    // Set up email options
    const mailOptions = {
        from: email,
        to: 'sh4d0w.h0g.22@gmail.com',
        subject: `Contact Form Message from ${name}`,
        text: message
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return res.status(500).json({ message: 'Error sending email', error });
        }
        res.status(200).json({ message: 'Email sent successfully!' });
    });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
