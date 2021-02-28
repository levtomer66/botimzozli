const app = require('../app')
const axios = require('axios')

app.get('/api', (req, res) => {
    axios.post(`https://${process.env.API_KEY}:${process.env.API_SECRET}@api.cloudinary.com/v1_1/${process.env.CLOUDNAME}/resources/search`, {"expression": "folder=bots/botimzozli"} ,{ headers: {'Access-Control-Allow-Origin' : '*'}})
    .then(response => {
        return res.status(200).send(response.data)
    })

})

module.exports = app
