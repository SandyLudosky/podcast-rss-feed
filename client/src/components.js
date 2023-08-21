import React, { useEffect, useMemo, useState } from "react";

function secondsToHMS(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const remainingSeconds = seconds % 60;

  return {
    hours: hours,
    minutes: minutes,
    seconds: remainingSeconds,
  };
}

function formatTimeUnit(unit) {
  return unit < 10 ? `0${unit}` : unit.toString();
}

function formatTime(_seconds) {
  const { hours, minutes, seconds } = secondsToHMS(_seconds);
  const formattedHours = formatTimeUnit(hours);
  const formattedMinutes = formatTimeUnit(minutes);
  const formattedSeconds = formatTimeUnit(seconds);

  return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
}

export const PodcastDetails = ({ item }) => {
  const published = useMemo(() => {
    const d = new Date(item?.date);
    return d.toLocaleDateString();
  }, [item]);
  const duration = useMemo(() => {
    return formatTime(item?.duration);
  }, [item]);
  if (item) {
    const { title, image: imageUrl, author } = item;

    return (
      <div className="podcast-summary">
        <div className="podcast-image">
          <img
            src={imageUrl}
            alt="Podcast Cover"
            width="100px"
            height="100px"
          />
        </div>
        <div className="podcast-details">
          <h2 className="podcast-title">{title}</h2>
          <ul>
            <li className="d-flex justify-content-between mb-1">
              <small>published : {published}</small>
              <small className="mx-2">duration: {duration}</small>
            </li>
            <li>
              {" "}
              <small>{author}</small>
            </li>
          </ul>
          <p></p>
        </div>
      </div>
    );
  }
};

export const PodcastSummary = ({ summary }) => {
  if (!summary) return null;
  return (
    <div className="my-3">
      <p className="h3">Podcast summary: </p>
      <p>{summary}</p>
    </div>
  );
};

export const PodcastPlayer = ({ item }) => {
  console.log(item?.type?.links[0]?.href);
  if (!item) return null;
  return (
    <div className="d-flex justify-items-center mt-3">
      <p className="align-self-center">Listen to podcast: </p>
      <figure className="mx-4">
        <audio controls src={item?.type?.links[0]?.href}>
          <a href={item?.type?.links[0]?.href}> Download audio </a>
        </audio>
      </figure>
    </div>
  );
};

export function ButtonSubmit() {
  return (
    <button
      type="submit"
      className="btn btn-primary d-flex align-items-center align-self-end"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        fill="currentColor"
        className="bi bi-rss"
        viewBox="0 0 16 16"
      >
        <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z" />
        <path d="M5.5 12a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm-3-8.5a1 1 0 0 1 1-1c5.523 0 10 4.477 10 10a1 1 0 1 1-2 0 8 8 0 0 0-8-8 1 1 0 0 1-1-1zm0 4a1 1 0 0 1 1-1 6 6 0 0 1 6 6 1 1 0 1 1-2 0 4 4 0 0 0-4-4 1 1 0 0 1-1-1z" />
      </svg>
      <span className="mx-2 ">Submit</span>
    </button>
  );
}

export const Form = React.forwardRef(({ submit, setRSS }, ref) => {
  return (
    <form onSubmit={submit}>
      <label>
        <span>Enter RSS Feed URL...</span>
        <input
          ref={ref}
          type="text"
          className="form-control my-2"
          onChange={(e) => setRSS(e.target.value)}
        />
      </label>
      <ButtonSubmit />
    </form>
  );
});

export const Loading = ({ loading, message }) => {
  const dots = useMemo(() => [".", "..", "..."], []);
  const [currentIndex, setIndex] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setIndex((i) => (i < dots.length - 1 ? i + 1 : 0));
    }, 800);
    return () => clearInterval(intervalId);
  }, [dots.length]);

  const loadingText = useMemo(() => {
    return `generating${dots[currentIndex]}`;
  }, [dots, currentIndex]);

  return (
    Boolean(loading && !message) && (
      <p className="h5 mt-4 text-primary">{loadingText}</p>
    )
  );
};

export const Error = ({ message }) => {
  if (!message) return null;
  return (
    <div className="alert alert-danger mt-4" role="alert">
      {message}
    </div>
  );
};
