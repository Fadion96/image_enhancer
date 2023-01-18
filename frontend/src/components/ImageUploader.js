import React, { useState, createRef } from 'react';
import {Link, useNavigate} from 'react-router-dom';
import PropTypes from 'prop-types';
import useToken from './useToken';

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
    const [image, setImage] = useState();
    const inputRef = createRef()

    const handleInput = () => {
        inputRef.current?.click();
      };

    const handleUpload = async e => {
        e.preventDefault();
        const data = new FormData();
        data.append("image", e.target.files[0])
        const image_data = await uploadImage(data, token);
        setImage(image_data.image)
      }


    return(
        <div >
            <img src={image}/>
            <div className="m-3">
                <label className="mx-3">Choose file: </label>
                <input ref={inputRef} className="d-none" type="file" onChange={handleUpload} />
                <button onClick={handleInput} className="btn btn-outline-primary">
                    Upload
                </button>
            </div>
        </div>
    )
  }
