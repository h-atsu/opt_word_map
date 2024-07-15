import React from 'react';
import Graph from './components/Graph';
import data from './data/list_opt_term.json';

function App() {
    return (
        <div style={{ width: '100vw', height: '100vh' }}>
            <Graph data={data} />
        </div>
    );
}

export default App;