import { fireEvent, render, screen } from '@testing-library/react'
import MyCheckbox from './create_check_box'

test('Initial conditions', () => {
    render(<MyCheckbox />)

    // Check that the checkbox starts out unchecked
    const checkbox = screen.getByRole('checkbox')
    expect(checkbox).not.toBeChecked()
  })

  test('After checking', () => {
    render(<MyCheckbox />)  
    // Check that the checkbox starts out unchecked
    const checkbox = screen.getByRole('checkbox')
    fireEvent.click(checkbox)
    expect(checkbox).toBeChecked()
  })