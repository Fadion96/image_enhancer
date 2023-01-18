import React, { useState } from 'react';
import {Link, useNavigate} from 'react-router-dom';
import PropTypes from 'prop-types';
import './Login.css';


async function loginUser(credentials) {
 return fetch('http://127.0.0.1:8000/accounts/login/', {
   method: 'POST',
   headers: {
     'Content-Type': 'application/json'
   },
   body: JSON.stringify(credentials)
 }).then(function (response) {
        if(response.status === 200){
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

export default function Login({ setToken }) {
  const [username, setUserName] = useState();
  const [password, setPassword] = useState();
    const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      username,
      password
    });
    if(token){
        setToken(token);
        navigate("/");
    }
  }

  return(
    <div className="login-wrapper">
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <label>
          <p>Username</p>
          <input type="text" onChange={e => setUserName(e.target.value)} />
        </label>
        <label>
          <p>Password</p>
          <input type="password" onChange={e => setPassword(e.target.value)} />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
      <h5> Need an account?</h5>
      <Link to='/registration'>
        <button type="submit">Register</button>
      </Link>

    </div>
  )
}

Login.propTypes = {
  setToken: PropTypes.func.isRequired
};
