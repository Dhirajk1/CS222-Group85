import React, { useState } from "react";
import Image from "next/image";
import logo from "./logo.png"
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
    <div className="wrapper" role="logo">
    <div className="logo">
      <Image className="img" src={logo} layout="intrinsic" alt="Company Logo"
      width = "1000"
      height = "1000"/>
    </div>
  </div>
  <div className="container has-background-link is-rounded">
    <form className="form" role="form" id="login" onSubmit={(e) => submitHandler(e)}>
        <h1 className="form__title is-size-1 has-text-primary-light">Login Below!</h1>
        {error != "" ? <div className="form__message--error">{error}</div> : ""}
        <div className="form__input-group">
          <input
            placeholder="Name"
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
          <input
            placeholder="Email"
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
          <input
            placeholder="Password"
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

        <input aria-label="button" className="button is-danger" type="submit" value="LOGIN"/>
    </form>
    </div>
    </div>
  );
}

export default LoginForm;
