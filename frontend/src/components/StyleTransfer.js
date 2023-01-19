import React, {createRef, useContext, useState } from 'react';
import useToken from './useToken';
import ImagesContext from './ImagesContext';

async function transferStyle(contentImage, styleImage, userToken) {
    return fetch('http://127.0.0.1:8000/image/enhance/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + userToken

      },
      body: JSON.stringify({
        'content_image': contentImage,
        'style_image' : styleImage
      })
    }).then(function (response) {
           if(response.status === 201){
               return response.json();
           }
           else {
               response.json().then((value) => {
                   alert(JSON.stringify(value))
               });
               return null
           }
       })
   }

export default function StyleTransfer() {
    const { token, setToken } = useToken();
    const [loading, setLoading] = useState(false);
    const [inputImage, setInputImage] = useState();
    const [styleImage, setStyleImage] = useState();
    const [resultImage, setResultImage] = useState();
    const [cImage, setcImage] = useState(1);
    const [sImage, setsImage] = useState(1);
    const { images, setImages } = useContext(ImagesContext);

    const handleTransfer = async e => {
        e.preventDefault();
        setLoading(true);
        const image_data = await transferStyle(cImage, sImage, token);
        if(image_data){
            image_data.image = "http://127.0.0.1:8000" + image_data.image
            setResultImage(image_data.image)
            setImages([...images, image_data])
        }
        setLoading(false);
      }

    const handleInputImage = async e => {
      setcImage(e.target.value)
      let img = images.find(x => x.id == e.target.value).image;
      setInputImage(img)
    }

    const handleStyleImage = async e => {
      setsImage(e.target.value)
      let img = images.find(x => x.id == e.target.value).image;
      setStyleImage(img)
    }

return(
    <div className="container text-center">
      <div className="row align-items-start">
      <div className="col m-2">
        <img src={inputImage} className="img-thumbnail" width="200" height="200"/>
        <h5>Choose input image</h5>
        <select className="form-select"  onChange={handleInputImage} defaultValue="1">
        {images && images.map((image) => (
          <option key={image.id} value={image.id}>{image.id}</option>
        ))}
        </select>
      </div>
      <div className="col m-2">
        <img src={resultImage} className="img-thumbnail" width="200" height="200"/>
        <h5>Result</h5>

      </div>
      </div>
      <div className="row align-items-start">
      <div className="col m-2">
        <img src={styleImage} className="img-thumbnail" width="200" height="200"/>
        <h5>Choose style image</h5>
        <select className="form-select" onChange={handleStyleImage} defaultValue="1">
        {images && images.map((image) => (
          <option key={image.id} value={image.id}>{image.id}</option>
        ))}
        </select>
      </div>
      <div className="col m-2 align-self-center">
        <button type="button" className="btn btn-primary" onClick={handleTransfer} disabled={loading} >
          {loading &&
            <>
              <span className="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
               Loading...
            </>
          }
          {!loading && <span>Transfer Style</span>}
        </button>
      </div>
      </div>
    </div>
  )
}
