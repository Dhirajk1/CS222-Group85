import * as React from 'react';

const App = () => {
  const [checked, setChecked] = React.useState(false);

  const handleChange = () => {
    setChecked(!checked);
  };

  return (
    <div>
      <Checkbox
        label="My Value"
        value={checked}
        onChange={handleChange}
      />

      <p>Is "My Value" checked? {checked.toString()}</p>
    </div>
  );
};

const Checkbox = ({ label, value, onChange }) => {
  return (
    <label>
      <input type="checkbox" checked={value} onChange={onChange} />
      {label}
    </label>
  );
};

export default App;