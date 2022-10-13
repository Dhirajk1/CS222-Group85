import React, { useState } from "react";
import Image from "next/image";
import logo from "./cs_222_logo.jpeg";
//Inspired by https://www.youtube.com/watch?v=7uKVFD_VMT8

interface Details {
  name: string;
  email: string;
  password: string;
  name1: string;
  name2: string;
  email1: string;
  email2: string;
  password1: string;
  password2: string;
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
  name1: "",
  name2: "",
  password1: "",
  password2: "",
  email1: "",
  email2: "",
  });

  const submitHandler = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    Login(details);
  };
  return (
  <div className="body">
    <div className="wrapper" role="logo">
    <div className="logo">
      <Image className="img" src={logo} layout="intrinsic" alt="Company Logo"
       width="200" height="200"/>
    </div>
  </div>
  <div className="container">
    <form className="form" role="form" id="login" onSubmit={(e) => submitHandler(e)}>
        <h1 className="form__title">Login</h1>
        {error != "" ? <div className="form__message--error">{error}</div> : ""}

        {/* username input area when logging in */}

        <div className="form__input-group">
          <label htmlFor="name">Username:</label>
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

        {/* email input area when logging in */}

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

        {/* password input area when logging in */}

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

       <input aria-label="button" className="form__button" type="submit" value="Login" />
       {/* <p><a href="http://www.google.com/">Don't have an Account? Create Account</a></p> */}
    </form>
    </div>

    <div className="container1">
    <form className="form" role="form" id="create_account" onSubmit={(e) => submitHandler(e)}></form>
    <h1 className="form__title">Create Account</h1>
        {error != "" ? <div className="form__message--error">{error}</div> : ""}

        {/* username input area when creating account */}

        <div className="form__input-group">
          <label htmlFor="name">Username:</label>
          <input
            type="text"
            name="name"
            aria-label="name"
            id="name"
            // autofocus="username"
            className="form__input"
            onChange={(e) => setDetails({ ...details, name1: e.target.value })}
            value={details.name1}
          />
        </div>

        {/* email input area when creating account */}

        <div className="form__input-group">
          <label htmlFor="name">Email:</label>
          <input
            type="text"
            name="name"
            aria-label="name"
            id="name"
            // autofocus="email address"
            className="form__input"
            onChange={(e) => setDetails({ ...details, email1: e.target.value })}
            value={details.email1}
          />
        </div>

        {/* confirm email input area when creating account */}

        <div className="form__input-group">
          <label htmlFor="name">Confirm Email:</label>
          <input
            type="text"
            name="name"
            aria-label="name"
            id="name"
            // autofocus="email address"
            className="form__input"
            onChange={(e) => setDetails({ ...details, email2: e.target.value })}
            value={details.email2}
          />
        </div>

        {/* password input area when creating account */}

        <div className="form__input-group">
          <label htmlFor="name">Password:</label>
          <input
            type="text"
            name="name"
            aria-label="name"
            id="name"
            // autofocus="email address"
            className="form__input"
            onChange={(e) => setDetails({ ...details, password1: e.target.value })}
            value={details.password1}
          />
        </div>

        {/* confirm password input area when creating account */}

        <div className="form__input-group">
          <label htmlFor="name">Confirm Password:</label>
          <input
            type="text"
            name="name"
            aria-label="name"
            id="name"
            // autofocus="email address"
            className="form__input"
            onChange={(e) => setDetails({ ...details, password2: e.target.value })}
            value={details.password2}
          />

          <input aria-label="button" className="form__button" type="submit" value="Create Account" />
        </div>

        </div>
    </div>
  );
}

export default LoginForm;
