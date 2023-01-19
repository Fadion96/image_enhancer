import React, {useEffect, useState} from 'react';
import ImageUploader from './ImageUploader';
import useToken from './useToken';
import ImagesContext from './ImagesContext';
import StyleTransfer from './StyleTransfer';


export default function Gallery() {
  const { token, setToken } = useToken();
  const [images, setImages] = useState();

  const image_context = { images, setImages};
  useEffect(() => {
    fetch('http://127.0.0.1:8000/image/',
    {
      method: 'GET',
      headers: {
          'Authorization': 'Token ' + token
      }
    }).then(function (response) {
      if(response.status === 200){
          response.json().then((value) => {
              setImages(value.results)
          });
      }
      else {
          response.json().then((value) => {
              alert(JSON.stringify(value))
          });
      }
    });

  }, [],);

  return(
    <div>
      <h2>Gallery</h2>
      <ImagesContext.Provider value={image_context}>
        <ImageUploader/>
        <StyleTransfer/>
      </ImagesContext.Provider>
      <div className="container text-center">
      <div className="row align-items-start">

      <div className="col">
      <h2>Uploaded images</h2>
        {images &&
          images.filter((image => (!image.is_result))).map((image) => (
            <li key={image.id}>
            <img src={image.image} className="img-thumbnail" width="200" height="200"/>
            <p>{image.id}</p>
          </li>
          ))}
      </div>
      <div className="col">
      <h2>Results of style transfer</h2>
        {images &&
          images.filter((image => (image.is_result))).map((image) => (
            <li key={image.id}>
            <img src={image.image} className="img-thumbnail" width="200" height="200"/>
            <p>{image.id}</p>
          </li>
          ))}
      </div>
      </div>
      </div>

    </div>
  );
}
