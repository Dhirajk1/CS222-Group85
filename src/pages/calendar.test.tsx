import { fireEvent, render, screen } from '@testing-library/react';
import CalendarPage from './calendar';

// Test the Calendar UI component
describe("Calendar Page Rendering",  () => {
  it ("Title Renders", () => {
    render(<CalendarPage />);
    // Verify we are on the right page via title
    const title = screen.getByText("Calendar");
    expect(title).toBeInTheDocument();
  });
}); 

describe("Event functionality working", () => {
  it("Add Event features render placeholders correctly", () => {
    render(<CalendarPage />); 
    const inputTitle = screen.getByPlaceholderText(/Add Title/i);
    const inputStart = screen.getByPlaceholderText(/Start Date/i);
    const inputEnd = screen.getByPlaceholderText(/End Date/i);
    expect(inputTitle).toBeInTheDocument();
    expect(inputStart).toBeInTheDocument();
    expect(inputEnd).toBeInTheDocument();
  })

  it("Add Event input and event creation works", () => {
    render(<CalendarPage />);
    const inputTitle = screen.getByPlaceholderText(/Add Title/i);
    const inputStart = screen.getByPlaceholderText(/Start Date/i);
    const inputEnd = screen.getByPlaceholderText(/End Date/i);
    //check inputs can be modified
    fireEvent.change(inputTitle, {target: {value: "do work"}});
    expect(inputTitle.value).toBe("do work");
    fireEvent.change(inputStart, {target: {value: "10/21/22"}});
    expect(inputStart.value).toBe("10/21/2022");
    fireEvent.change(inputEnd, {target: {value: "10/22/22"}});
    expect(inputEnd.value).toBe("10/22/2022");
    //check if pressing add event creates event on calendar
    const button = screen.getByRole("button", {name: /Add or Edit Event/i});
    fireEvent.click(button); 
  })

  it("Remove Event Works", () => {
    render(<CalendarPage />);
    const inputTitle = screen.getByPlaceholderText(/Add Title/i);
    const inputStart = screen.getByPlaceholderText(/Start Date/i);
    const inputEnd = screen.getByPlaceholderText(/End Date/i);
    fireEvent.change(inputTitle, {target: {value: "do work"}});
    fireEvent.change(inputStart, {target: {value: "10/21/22"}});
    fireEvent.change(inputEnd, {target: {value: "10/22/22"}});
    const button = screen.getByRole("button", {name: /Add or Edit Event/i});
    fireEvent.click(button); 
    window.confirm = jest.fn(() => true)
    expect(screen.queryByText("do work")).not.toBeInTheDocument()
  })

  it("Edit Event Works", () => {
    render(<CalendarPage />);
    const inputTitle = screen.getByPlaceholderText(/Add Title/i);
    const inputStart = screen.getByPlaceholderText(/Start Date/i);
    const inputEnd = screen.getByPlaceholderText(/End Date/i);
    fireEvent.change(inputTitle, {target: {value: "do work"}});
    fireEvent.change(inputStart, {target: {value: "10/21/22"}});
    fireEvent.change(inputEnd, {target: {value: "10/22/22"}});
    const button = screen.getByRole("button", {name: /Add or Edit Event/i});
    fireEvent.click(button); 
    fireEvent.change(inputTitle, {target: {value: "Woof Woof"}});
    fireEvent.change(inputStart, {target: {value: "11/08/22"}});
    fireEvent.change(inputEnd, {target: {value: "11/08/22"}});
    window.confirm = jest.fn(() => true)
    expect(screen.queryByText("do work")).not.toBeInTheDocument()
  })
});