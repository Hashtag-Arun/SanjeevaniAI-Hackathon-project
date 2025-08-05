import React, { useEffect, useState } from 'react';

function App() {
  const [stats, setStats] = useState({});

  useEffect(() => {
    fetch("http://localhost:8000/blood-stats")
      .then(res => res.json())
      .then(data => setStats(data));
  }, []);

  return (
    <div>
      <h1>Blood Group Summary</h1>
      <ul>
        {stats.summary &&
          Object.entries(stats.summary).map(([group, count]) => (
            <li key={group}>{group}: {count}</li>
          ))}
      </ul>
      {stats.prediction && (
        <>
          <p><b>Most Common:</b> {stats.prediction.most_common}</p>
          <p><b>Rare Groups:</b> {stats.prediction.critical.join(", ")}</p>
        </>
      )}
    </div>
  );
}

export default App;
