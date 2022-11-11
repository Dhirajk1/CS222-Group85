import { check } from 'prettier';
import * as React from 'react';
import { text } from 'stream/consumers';

//this is the checkbox type that I created
const MyCheckbox = () => {
  const [checked, setChecked] = React.useState(false);
  //toggles the state of checked
  const handleChange = () => {
    setChecked(!checked);
  };
  //handles changes and also displays image if checkbox is clicked
  return (
    <div>
      <label>
        <Checkbox
          label="My Value"
          value={checked}
          onChange={handleChange}
        />
        My Value
      </label>
      <p>Is &lsquo;My Value&lsquo; checked? {checked.toString()}</p>
      {
        checked? <img alt="happy face" src={'./happy.jpeg'}/> :null
      }
    </div>
  );
};

const Checkbox = ({label, value, onChange }: any) => {
  return (
    <label>
      <input type="checkbox" checked={value} onChange={onChange} />
      {label}
    </label>
  );
};

export default MyCheckbox;