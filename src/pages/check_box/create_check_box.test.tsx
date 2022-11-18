import { fireEvent, getByAltText, render, screen } from '@testing-library/react'
import MyCheckbox from './create_check_box'

test('Initial conditions', () => {
    render(<MyCheckbox />)

    // Check that the checkbox starts out unchecked
    const checkboxes = screen.getAllByRole('checkbox')
    expect(checkboxes[0]).not.toBeChecked()
    expect(checkboxes[1]).not.toBeChecked()
  })

  test('After checking', () => {
    render(<MyCheckbox />)  
    // Check that the checkbox shows checked
    const checkboxes = screen.getAllByRole('checkbox')
    fireEvent.click(checkboxes[0])
    expect(checkboxes[0]).toBeChecked()
    expect(checkboxes[1]).not.toBeChecked()
  })
    
  it('displays a happy face only if both are checked', () => {
    //only displays happy face if checkbox is clicked
      render(<MyCheckbox />)
      const checkboxes = screen.getAllByRole('checkbox')
      fireEvent.click(checkboxes[0])
      fireEvent.click(checkboxes[1])
      const displayedImage = screen.getByRole('img');
      expect(displayedImage).toBeVisible();
  })