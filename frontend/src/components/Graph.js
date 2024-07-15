import React from 'react';
import CytoscapeComponent from 'react-cytoscapejs';

function Graph({ data }) {
    const elements = data.flatMap(item => [
        { 
            data: { 
                id: item.term, 
                label: item.term,
                url: item.url  // Add URL to node data
            } 
        },
        ...item.list_related_term.map(relatedTerm => ({
            data: { 
                id: `${item.term}-${relatedTerm}`,
                source: item.term, 
                target: relatedTerm 
            }
        }))
    ]);

    const layout = {
        name: 'cose',
        randomize: true,
        nodeRepulsion: 10000,
        idealEdgeLength: 100,
        nodeOverlap: 20,
        padding: 30
    };

    const stylesheet = [
        {
            selector: 'node',
            style: {
                "background-color": "#1976d2",
                shape: "round-rectangle",
                'label': 'data(label)',
                'text-valign': 'center',
                'text-halign': 'center',
                'font-size': '12px',
                'width': 'label',
                'height': 'label',
                'padding': '10px',
                'text-wrap': 'wrap',
                'text-max-width': '100px'
            }
        },
        {
            selector: "node[label]",
            style: {
              label: "data(label)",
              "font-size": "12",
              color: "white",
              "text-halign": "center",
              "text-valign": "center",
            },
        },
        {
            selector: 'edge',
            style: {
                'width': 1,
                'curve-style': 'bezier',
                'line-color': '#ccc',
                'target-arrow-shape': 'triangle',  // Add arrow for directed graph
                'target-arrow-color': '#ccc'
            }
        }
    ];

    const cyRef = React.useRef(null);

    const handleNodeClick = (event) => {
        const node = event.target;
        const url = node.data('url');
        if (url) {
            window.open(url, '_blank');
        }
    };

    return (
        <CytoscapeComponent
            elements={elements}
            layout={layout}
            stylesheet={stylesheet}
            style={{ width: '100%', height: '100%' }}
            cy={(cy) => {
                cyRef.current = cy;
                cy.on('tap', 'node', handleNodeClick);
            }}
        />
    );
}

export default Graph;