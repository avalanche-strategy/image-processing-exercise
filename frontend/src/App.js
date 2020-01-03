import React, { useState } from 'react';
import Api from './api.js';
import './App.css';

const onSubmit = (event, file) => {
  const data = new FormData()
  data.append('file', file)

  Api.post('/image_processor/image/convert-bw/', data).then(response => {
    console.log(response);
  });

  event.preventDefault();
};

const onSelectFile = (event, setFile, setImage) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = function (e) {
      setImage(e.target.result);
  };

  reader.readAsDataURL(file);

  setFile(file);
}

function App() {
  const [file, setFile] = useState(null);
  const [image, setImage] = useState(null)

  return (
    <div className="App">
      {image && <img style={{ maxWidth: '400px'}} src={image} />}
      <form onSubmit={(event) => onSubmit(event, file)}>
        <label htmlFor="image-upload">Choose a picture</label>
        <input
          id='image-upload'
          type='file'
          accept='image/png'
          onChange={event => onSelectFile(event, setFile, setImage)}
        />
        <button type='submit'>Upload</button>
      </form>
    </div>
  );
}

export default App;
