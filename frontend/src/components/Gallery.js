import React, {useEffect, useState} from 'react';
import ImageUploader from './ImageUploader';
import useToken from './useToken';
import ImagesContext from './ImagesContext';


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
          </ImagesContext.Provider>
          {images &&
            images.map((image) => (
            <li key={image.id}>
              <img src={image.image} style={{maxWidth : '256px'}}/>
            </li>
          ))}


     </div>
  );
}
