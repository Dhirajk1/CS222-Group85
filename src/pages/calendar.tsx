import { NextPage } from "next";
import { Calendar, dateFnsLocalizer } from "react-big-calendar";
import format from "date-fns/format";
import parse from "date-fns/parse";
import startOfWeek from "date-fns/startOfWeek";
import getDay from "date-fns/getDay";
import "react-big-calendar/lib/css/react-big-calendar.css";
import { useState, useEffect } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import fetch from "cross-fetch";
import { useRouter } from "next/router";

const locales: object = {
  "en-US": require("date-fns/locale/en-US"),
};
// Disables to create specific instance of our config
// eslint-disable-next-line @typescript-eslint/no-unsafe-call
const localizer = dateFnsLocalizer({
  format,
  parse,
  startOfWeek,
  getDay,
  locales,
});
interface event {
  title: string;
  allDay?: boolean;
  start: Date;
  end: Date;
}

const userEvents: event[] = []; //variable user events

const CalendarPage: NextPage = () => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [newEvent, setNewEvent] = useState({
    title: "",
    start: new Date(),
    end: new Date(),
  });
  const [allEvents, setAllEvents] = useState(userEvents);
  const router = useRouter();
  const username = router
    ? router.query.username
      ? router.query.username
      : ""
    : "";
  const formInput = username as unknown as string;

  //routing for find events
  useEffect(() => {
    const formData = new FormData();
    formData.append("user_id", formInput);
    fetch("http://localhost:5000/events/find", { method: "GET" })
      .then((response) => response.json())
      .then((res) => setAllEvents(res))
      .catch(Error);
  });

  //routing and adding events to calendar
  const AddEvent = () => {
    const formData = new FormData();
    formData.append("user_id", formInput);
    fetch("http://localhost:5000/events/add", {
      method: "POST",
      body: formData,
    }).catch(Error);
    setAllEvents([...allEvents, newEvent]);
  };

  //routing and removing events from calendar
  const RemoveEvent = (event) => {
    const formData = new FormData();
    formData.append("user_id", formInput)
    formData.append("date", event.start)
    fetch("http://localhost:5000/events/remove", {
      method: "POST",
      body: formData,
    }).catch(Error)
    const current_events = [...allEvents]
    current_events.splice(current_events.indexOf(event), 1)
    setAllEvents(current_events)
  }

  //routing and editing evetns from calendar
  const EditEvent = (event) => {
    const formData = new FormData();
    formData.append("user_id", formInput)
    formData.append("date", event.start)
    formData.append("detail", event.title)
    fetch("http://localhost:5000/events/edit", {
      method: "POST",
      body: formData,
    }).catch(Error)
    const current_events = [...allEvents]
    current_events.splice(current_events.indexOf(event), 1)
    setAllEvents([...current_events, newEvent])
  }

  //allows user to choose to remove/edit event when event is clicked
  const handleEventSelection = (event) =>{
    const remove = window.confirm("Do you want to remove this event?")
    if (remove) RemoveEvent(event)
    else {
      const edit = window.confirm("Do you want to edit this event?")
      if (edit) EditEvent(event)
    }
  };

  //displays calendar page and add/edit event fields
  return (
    <div>
      <h1>Calendar</h1>
      <h2> Add/Edit Event </h2>
      <p> To Edit: Update fields and click the event you want edited.
                   Will be prompted to remove; cancel that to edit.
      </p>
      <p>Current User is: {formInput}</p>
      <div>
        <input
          type="text"
          placeholder="Add Title"
          style={{ width: "20%", marginRight: "10px" }}
          value={newEvent.title}
          onChange={(e) => setNewEvent({ ...newEvent, title: e.target.value })}
        />
        <DatePicker
          placeholderText="Start Date"
          selected={newEvent.start}
          onChange={(date) =>
            setNewEvent({ ...newEvent, start: date ? date : newEvent.start })
          }
        />
        <DatePicker
          placeholderText="End Date"
          selected={newEvent.end}
          onChange={(date) =>
            setNewEvent({ ...newEvent, end: date ? date : newEvent.end })
          }
        />
        <button style={{ marginTop: "10px" }} onClick={AddEvent}>
          Add or Edit Event
        </button>
      </div>
      <Calendar
        localizer={localizer}
        events={allEvents}
        startAccessor="start"
        endAccessor="end"
        style={{ height: "1000px", margin: "50px" }}
        onSelectEvent={handleEventSelection}
      />
    </div>
  );
};
export default CalendarPage;
