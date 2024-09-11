const { createCanvas } = require('canvas');
const Chart = require('chart.js');
const fs = require('fs');
xw
async function generateChart(projections) {
    const width = 800;
    const height = 600;
    const canvas = createCanvas(width, height);
    const ctx = canvas.getContext('2d');

    const weeklyProjections = projections.map(projection => projection.points); // Adjust based on actual data structure
    const labels = projections.map(projection => `Week ${projection.week}`); // Adjust based on actual data structure

    const configuration = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Team Projections',
                    data: weeklyProjections,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false,
                },
            ],
        },
    };

    new Chart(ctx, configuration);

    const buffer = canvas.toBuffer('image/png');
    fs.writeFileSync('team_projections_chart.png', buffer);
    console.log('Chart saved as team_projections_chart.png');
}

// Fetch data and generate chart as previously outlined
