import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {Link, useNavigate} from 'react-router-dom';
import './Login.css';

async function registerUser(credentials) {
 return fetch('http://127.0.0.1:8000/accounts/registration', {
   method: 'POST',
   headers: {
     'Content-Type': 'application/json'
   },
   body: JSON.stringify(credentials)
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

export default function Register({ setToken }) {
  const [username, setUserName] = useState();
  const [email, setEmail] = useState();
  const [password1, setPassword1] = useState();
  const [password2, setPassword2] = useState();
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await registerUser({
      username,
      email,
      password1,
      password2
    });
    if(token){
        setToken(token);
        navigate("/");
    }
  }

  return(
    <div className="login-wrapper">
      <h1>Registration</h1>
      <form onSubmit={handleSubmit}>
        <label>
          <p>Username</p>
          <input type="text" onChange={e => setUserName(e.target.value)} />
        </label>
        <label>
          <p>Email</p>
          <input type="text" onChange={e => setEmail(e.target.value)} />
        </label>
        <label>
          <p>Password</p>
          <input type="password" onChange={e => setPassword1(e.target.value)} />
        </label>
        <label>
          <p>Confirm password</p>
          <input type="password" onChange={e => setPassword2(e.target.value)} />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
      <h5> Already registred?</h5>
      <Link to='/login'>
        <button type="submit">Login</button>
      </Link>
    </div>
  )
}

Register.propTypes = {
  setToken: PropTypes.func.isRequired
};
