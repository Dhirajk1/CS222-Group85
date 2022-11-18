import React, { useState} from 'react'
import { Link } from 'react-router-dom'

const NavBar = () => {
const [ show, setShow ] = useState(false)
function showSwitch() {
return setShow(!show)

}
return (

<div className='navbar'>

 <div className="logo">
CALENDAR
 </div>

<div className={show ? "links active": "links"}>
<Link to ="/"> Home </Link>
<Link to ="/"> Points </Link>
<Link to ="/"> About </Link>
<Link to ="/"> Rewards </Link>
</div>

<div onClick={()=> showSwitch} className={show ? "bars-button 26.   active": "bars-button"}>
<span></span>
<span></span>
<span></span>
</div>
</div>
)
}
export default NavBar