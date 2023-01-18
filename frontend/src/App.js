import React from 'react';
import './App.css';
import { BrowserRouter, Route, Routes  } from 'react-router-dom';
import Gallery from './components/Gallery';
import Login from './components/Login';

import useToken from './components/useToken';

function App() {
  const { token, setToken } = useToken();
  if(!token) {
    return <Login setToken={setToken} />
  }
  return (
    <div className="wrapper">
      <h1>Application</h1>
      <BrowserRouter>
        <Routes>
          <Route path="/gallery" element={<Gallery />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
