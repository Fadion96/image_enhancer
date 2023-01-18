import {
    Navigate,
  } from 'react-router-dom';
import useToken from './useToken';

  const ProtectedRoute = ({ children }) => {
    const { token, setToken } = useToken();

    if (!token) {
      return <Navigate to="/login" replace />;
    }

    return children;
  };

  export default ProtectedRoute;
