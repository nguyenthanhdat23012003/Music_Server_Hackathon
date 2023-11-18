// Import các modules và tạo một instance của Express
const express = require("express");
const app = express();
const port = 4000;
const mqtt = require("mqtt");
const client = mqtt.connect("mqtt://broker.hivemq.com:1883");
const cors = require("cors");
var bodyParser = require("body-parser");
var jsonParser = bodyParser.json();
app.use(cors()); // Sử dụng cors middleware
// Tạo một endpoint GET với đường dẫn '/'
app.use(bodyParser.json());

app.post("/", (req, res) => {
  //   const message = {
  //     hour: req.body.message.hours,
  //     minute: req.body.message.minutes,
  //     file: req.body.message.file,
  //   };
  console.log(req.body);
  //   console.log(JSON.stringify(message));
  client.publish("/hapt/Pub", req.body.message);
  res.send("Hello, World! This is your API endpoint.");
});

// Lắng nghe cổng và khởi động máy chủ
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
