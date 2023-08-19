import React, { useState } from "react";
import axios from "axios";

function App() {
  const [rss, setRss] = useState("");
  const [transcript, setTranscript] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRssSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/transcribe/", {
        rss,
      });
      setTranscript(response.data);
      setLoading(false);
    } catch (error) {
      console.error(error);
    }
  };

  const handleTranscriptSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/summarize/", {
        content: transcript,
      });
      setSummary(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        flexDirection: "column",
        marginTop: "40px",
      }}
    >
      {loading && <h1>Loading...</h1>}
      <form onSubmit={handleRssSubmit}>
        <label>
          RSS Feed URL:
          <input
            type="text"
            value={rss}
            onChange={(e) => setRss(e.target.value)}
          />
        </label>
        <button type="submit" className="mx-2">
          Transcribe
        </button>
      </form>
      {transcript && (
        <form onSubmit={handleTranscriptSubmit}>
          <label>
            Transcript:
            <textarea
              value={transcript}
              onChange={(e) => setTranscript(e.target.value)}
            />
          </label>
          <button type="submit" className="mx-2">
            Summarize
          </button>
        </form>
      )}
      {summary && (
        <div>
          <h2>Summary:</h2>
          <p>{transcript}</p>
        </div>
      )}
    </div>
  );
}

export default App;
