import { render, screen } from "@testing-library/react";
import CalendarPage from "./calendar";

// eslint-disable-next-line @typescript-eslint/no-var-requires
const myRouter = jest.spyOn(require("next/router"), "useRouter");
describe("Calendar Page Rendering", () => {
  it("Title Renders", () => {
    myRouter.mockImplementationOnce(() => ({
      query: { username: "Ichigo Kurosaki" },
    }));
    render(<CalendarPage />);
    const context = screen.getByText(/Ichigo Kurosaki/);
    expect(context).toBeInTheDocument();
  });
});
