import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

import React, { useState } from "react";
import Image from "next/image";
import logo from "./cs_222_logo.jpeg";
//Inspired by https://www.youtube.com/watch?v=7uKVFD_VMT8

interface Details {
  name: string;
  email: string;
  password: string;
}
interface IProps {
  Login: (arg0: Details) => void;
  error: string;
}
function LoginForm({ Login, error }: IProps) {
  const [details, setDetails] = useState<Details>({
    name: "",
    email: "",
    password: "",
  });

  const submitHandler = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    Login(details);
  };
  return (
  <div className="body">
    {/* <p><a href="http://localhost:3000/creator">Don&apos;t have an Account? Create Account</a></p> */}
    <div className="wrapper" role="logo">
    <div className="logo">
      <Image className="img" src={logo} layout="intrinsic" alt="Company Logo"
        width="200" height="200"/>
    </div>
  </div>
  <div className="navBar">
    
  </div>
  <div className="container">
    <form className="form" role="form" id="login" onSubmit={(e) => submitHandler(e)}>
        <h1 className="form__title">Login</h1>
        {error != "" ? <div className="form__message--error">{error}</div> : ""}
        <div className="form__input-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            name="name"
            aria-label="name"
            id="name"
            className="form__input"
            onChange={(e) => setDetails({ ...details, name: e.target.value })}
            value={details.name}
          />
        </div>

        <div className="form__input-group">
          <label htmlFor="email">Email:</label>
          <input
            type="text"
            name="email"
            id="email"
            aria-label="email"
            className="form__input"
            onChange={(e) => setDetails({ ...details, email: e.target.value })}
            value={details.email}
          />
        </div>

        <div className="form__input-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            name="password"
            id="password"
            aria-label="password"
            className="form__input"
            onChange={(e) =>
              setDetails({ ...details, password: e.target.value })
            }
            value={details.password}
          />
        </div>

        <input aria-label="button" className="form__button" type="submit" value="LOGIN" />
        {/* <input aria-label="button" className="form__button" type="submit" value="Create" /> */}
        <p><a href="http://localhost:3000/creator">Don&apos;t have an Account? Create Account</a></p>
    </form>
    </div>
    </div>
  );
}

export default LoginForm;