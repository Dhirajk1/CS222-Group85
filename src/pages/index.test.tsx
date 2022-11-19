import { fireEvent, render, screen } from '@testing-library/react'
import Home from '.'
describe('Login Rendering', () => {
  it('Correct Login', () => {
    render(<Home />);
    let form = screen.getByRole('form');

    expect(form).toBeInTheDocument();
    form = screen.getByLabelText('name')
    fireEvent.change(form, {target: {value: "John Cena"}});
    form = screen.getByLabelText('email')
    fireEvent.change(form, {target: {value: "dhiraj2@illinois.edu"}});
    form = screen.getByLabelText('password');
    fireEvent.change(form, {target: {value: "cs222-group85"}}); 
    const button = screen.getByLabelText("button");
    fireEvent(button, new MouseEvent('click', {
      bubbles: true,
      cancelable: true,
    }));
    const res = screen.getByText("Welcome John Cena");
    expect(res).toBeInTheDocument();
  })
})