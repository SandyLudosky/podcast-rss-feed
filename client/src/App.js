import React, { useState, useRef } from "react";
import axios from "axios";
import {
  Form,
  Loading,
  PodcastDetails,
  PodcastSummary,
  PodcastPlayer,
  Error,
} from "./components";
import fixture from "./fixture";
import "./App.css";

function App() {
  const ref = useRef();
  const [rss, setRSS] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleRssSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    /*
    for testing
      setTimeout(() => {
        setResult(fixture);
        setLoading(false);
      }, 5000);
    */

    try {
      const response = await axios.post("transcribe/", {
        rss,
      });
      setResult(response.data);
      setLoading(false);
      ref.current.value = "";
    } catch (error) {
      setError(error);
    }
  };
  return (
    <div className="mt-5 App-container">
      <Form ref={ref} submit={handleRssSubmit} setRSS={setRSS} />
      <Loading loading={loading} {...error} />
      <PodcastDetails {...result} />
      <PodcastSummary {...result} />
      <PodcastPlayer {...result} />
      <Error {...error} />
    </div>
  );
}

export default App;
