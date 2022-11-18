import { check } from 'prettier';
import * as React from 'react';
import { text } from 'stream/consumers';

//this is the checkbox type that I created
const MyCheckbox = () => {
  const [checked1, setChecked1] = React.useState(false);
  const [checked2, setChecked2] = React.useState(false);
  //toggles the state of checked
  const handleChangeOne = () => {
    setChecked1(!checked1);
  };
  //handles second checkbox
  const handleChangeTwo = () => {
    setChecked2(!checked2);
  };
  //handles changes and also displays image if checkbox is clicked
  return (
    <div>
      <label>
        <Checkbox
          label="My Value"
          value={checked1}
          onChange={handleChangeOne}
        />
        My Value
      </label>
      <label>
        <Checkbox
          label="Value 2"
          value={checked2}
          onChange={handleChangeTwo}
        />
        Value 2
      </label>
      <p>Is &lsquo;My Value&lsquo; checked? {checked1.toString()}</p>
      {
        checked1?
        (
            checked2? <img alt="happy face" src={'./happy.jpeg'}/> :null
        ):null
      }
    </div>
  );
};
//template for future checkboxes
const Checkbox = ({label, value, onChange }: any) => {
  return (
    <label>
      <input type="checkbox" checked={value} onChange={onChange} />
      {label}
    </label>
  );
};

export default MyCheckbox;