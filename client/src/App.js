import React, { useState, useRef } from "react";
import axios from "axios";
import { Form, Loading, PodcastDetails, PodcastSummary } from "./components";
import fixture from "./fixture";
import "./App.css";

function App() {
  const ref = useRef();
  const [rss, setRSS] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleRssSubmit = async (e) => {
    setLoading(true);
    setResult({});
    e.preventDefault();
    try {
      const response = await axios.post("transcribe/", {
        rss,
      });
      setResult(response.data);
      setLoading(false);
      ref.current.value = "";
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className="mt-5 App-container">
      <Form ref={ref} submit={handleRssSubmit} setRSS={setRSS} />
      <Loading loading={loading} />
      <PodcastDetails {...result} />
      <PodcastSummary {...result} />
    </div>
  );
}

export default App;
