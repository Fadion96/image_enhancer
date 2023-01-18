import React from 'react';
import './App.css';
import {Route, Routes} from 'react-router-dom';
import Gallery from './components/Gallery';
import Login from './components/Login';
import Register from './components/Registration';
import ProtectedRoute from './components/ProtectedRoute';

import useToken from './components/useToken';

function App() {
  const { token, setToken } = useToken();

  return (

    <div className="wrapper">
      <h1>Application</h1>
        <Routes>
        <Route
            path="/"
            element={
                <ProtectedRoute>
                  <Gallery />
                </ProtectedRoute>
              }
            />
          <Route path="/login" element={<Login setToken={setToken} />}/>
          <Route path="/registration" element={<Register setToken={setToken} />}/>
          <Route
            path="/gallery"
            element={
                <ProtectedRoute>
                  <Gallery />
                </ProtectedRoute>
              }
            />
        </Routes>
    </div>
  );
}

export default App;
