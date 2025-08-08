// src/App.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Login from './components/Login';

axios.defaults.withCredentials = true;  // ensures cookies are sent with requests

const App = () => {
  const [user, setUser] = useState(null);

  const fetchMe = async () => {
    try {
      const res = await axios.get('http://localhost:8000/me');
      setUser(res.data);
    } catch (err) {
      setUser(null);
    }
  };

  const handleLogout = async () => {
    await axios.post('http://localhost:8000/logout');
    setUser(null);
  };

  useEffect(() => {
    fetchMe();
  }, []);

  return (
    <div>
      {user ? (
        <>
          <p>Welcome, {user.user_id}</p>
          <p>Your role: {user.role}</p>
          <p>debug1 : {JSON.stringify(user.user.user_id)}</p>
          <p>debug2 : {JSON.stringify(user.user.role)}</p>
          <p>{JSON.stringify(user)}</p>
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <Login onLogin={fetchMe} />
      )}
    </div>
  );
};

export default App;
