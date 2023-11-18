"use client";
import React, { useState } from "react";
import mqtt from "mqtt";

const AdminPage: React.FC = () => {
  const [time, setTime] = useState({
    hour: "",
    minute: "",
    file: " test",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setTime((prevTime) => ({
      ...prevTime,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const message = JSON.stringify(time);
    const rawResponse = await fetch("http://localhost:4000", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    });
  };

  return (
    <>
      <div className="p-4">
        <div>hello</div>
        <form
          onSubmit={handleSubmit}
          className="mt-4 p-4 bg-gray-200 rounded-md"
        >
          <div className="mb-4">
            <label className="block mb-2">Hours:</label>
            <input
              type="number"
              name="hour"
              value={time.hour}
              onChange={handleChange}
              className="border border-gray-400 p-2 rounded-md w-full"
              min="0"
              max="23"
            />
          </div>
          <div className="mb-4">
            <label className="block mb-2">Minutes:</label>
            <input
              type="number"
              name="minute"
              value={time.minute}
              onChange={handleChange}
              className="border border-gray-400 p-2 rounded-md w-full"
              min="0"
              max="59"
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 text-white py-2 px-4 rounded-md w-full"
          >
            Submit
          </button>
        </form>
      </div>
    </>
  );
};

export default AdminPage;
