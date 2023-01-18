import React, {createRef, useContext } from 'react';
import useToken from './useToken';
import ImagesContext from './ImagesContext';

async function uploadImage(data, token) {
    return fetch('http://127.0.0.1:8000/image/', {
      method: 'POST',
      headers: {
        'Authorization': 'Token ' + token

      },
      body: data
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


export default function ImageUploader() {
    const { token, setToken } = useToken();
    const { images, setImages } = useContext(ImagesContext);
    const inputRef = createRef();

    const handleInput = () => {
        inputRef.current?.click();
      };

    const handleUpload = async e => {
        e.preventDefault();
        const data = new FormData();
        data.append("image", e.target.files[0])
        const image_data = await uploadImage(data, token);
        if(image_data){
            setImages([...images, image_data])
        }
      }


    return(
        <div >
            <div className="m-3">
                <label className="mx-3">Choose file: </label>
                <input ref={inputRef} className="d-none" type="file" onChange={handleUpload} accept="image/*"/>
                <button onClick={handleInput} className="btn btn-outline-primary">
                    Upload
                </button>
            </div>
        </div>
    )
  }
