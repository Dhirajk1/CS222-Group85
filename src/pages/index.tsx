import type { NextPage } from "next";
import { useState } from "react";
import LoginForm from "../components/LoginForm";

import { useRouter } from 'next/router'
const Home: NextPage = () => {
  const router = useRouter()
  interface Details {
    name: string;
    email: string;
    password: string;
  }
  const admin = {
    email: "dhiraj2@illinois.edu",
    password: "cs222-group85",
  };

  const [user, setUser] = useState({ name: "", email: "" });
  const [error, setError] = useState(""); // invalid login handler

  const Login = async (details: Details) => {
    if (details.email === admin.email && details.password == admin.password) {
      setUser({
        name: details.name,
        email: details.email,
      });
    } else {
        console.log("Sending Request")
        const formData  = new FormData();
        formData.append("name", details.name);
        formData.append("email", details.email);
        formData.append("password", details.password);
        const response = await fetch("http://localhost:5000/login", 
                                    {method: "POST", body: formData});
        console.log("got response")
        console.log(response.status);
        const resJson = response;
        if (resJson.status === 201) {
          setUser({
            name: details.name,
            email: details.email,
          });
          await router.push({pathname: 'calendar/', 
                            query: { username: details.name }});
        } else {
          setError("Invalid Login");
      }
    }
  };
  const Logout = () => {
    setUser({
      name: "",
      email: "",
    });
    setError("");
  };
  return (
    <div className="Home">
      {user.email != "" ? (
        <div className="welcome">
          <h2 aria-label="Welcome">
            Welcome {user.name}
          </h2>
          <button onClick={Logout}>Logout</button>
        </div>
      ) : (
       <LoginForm Login={Login} error={error} />
      )}
    </div>
  );
};
export default Home;
