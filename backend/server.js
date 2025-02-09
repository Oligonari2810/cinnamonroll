// backend/server.js
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hola, este es el backend de Cinnamoroll');
});

app.listen(port, () => {
  console.log(`Servidor corriendo en el puerto ${port}`);
});
