import * as React from 'react';

const MyCheckbox = () => {
  const [checked, setChecked] = React.useState(false);

  const handleChange = () => {
    setChecked(!checked);
  };

  return (
    <div>
      <label>
        <input
          type="checkbox"
          checked={checked}
          onChange={handleChange}
        />
        My Value
      </label>

      <p>Is &lsquo;My Value&lsquo; checked? {checked.toString()}</p>
    </div>
  );
};

export default MyCheckbox;