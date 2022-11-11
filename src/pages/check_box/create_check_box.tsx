import { check } from 'prettier';
import * as React from 'react';
import { text } from 'stream/consumers';

const MyCheckbox = () => {
  const [checked, setChecked] = React.useState(false);

  const handleChange = () => {
    setChecked(!checked);
  };

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
      {/* <p>checked? {checked.toString() ? <img alt="happy face" src={'./happy.jpeg'}/> : "false"}</p> */}
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