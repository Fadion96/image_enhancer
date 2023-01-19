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
        <div className="mb-3">
          <label  className="form-label">Username</label>
          <input type="text" className="form-control" onChange={e => setUserName(e.target.value)} />
        </div>
        <div className="mb-3">
          <label  className="form-label">Email</label>
          <input type="email" className="form-control" onChange={e => setEmail(e.target.value)} />
        </div>
        <div className="mb-3">
          <label className="form-label">Password</label>
          <input type="password" className="form-control" onChange={e => setPassword1(e.target.value)} />
        </div>
        <div className="mb-3">
          <label className="form-label">Confirm password</label>
          <input type="password" className="form-control" onChange={e => setPassword2(e.target.value)} />
        </div>
        <div>
          <button type="submit" className="btn btn-primary">Submit</button>
        </div>
      </form>
      <div className="form-text">Already registred?</div>
      <Link to='/login'>
        <button type="submit" className="btn btn-secondary btn-sm">Login</button>
      </Link>
    </div>
  )
}

Register.propTypes = {
  setToken: PropTypes.func.isRequired
};
