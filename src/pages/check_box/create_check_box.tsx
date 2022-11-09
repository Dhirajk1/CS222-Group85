import * as React from 'react';

const MyCheckbox = () => {
  const [checked, setChecked] = React.useState(false);

  const handleChange = () => {
    setChecked(!checked);
    <img src="./happy.jpg" height="200" width="200"></img>
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