const proxy = require('http-proxy-middleware');
module.exports = app => 
    {  app.use(proxy('/api', 
        {target: process.env.FLASK_URL || 'http://127.0.0.1:5000'  
    }));
};