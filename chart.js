const { ChartJSNodeCanvas } = require('chartjs-node-canvas');
const fs = require('fs');

const width = 800; // Width of the chart
const height = 600; // Height of the chart

const chartJSNodeCanvas = new ChartJSNodeCanvas({ width, height });

// Example data from your projections
async function generateChart(projections) {
    const weeklyProjections = projections.map(projection => projection.points); // Adjust as necessary
    const labels = projections.map(projection => `Week ${projection.week}`); // Adjust as necessary

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

    try {
        const imageBuffer = await chartJSNodeCanvas.renderToBuffer(configuration);
        fs.writeFileSync('team_projections_chart.png', imageBuffer);
        console.log('Chart saved as team_projections_chart.png');
    } catch (error) {
        console.error('Error generating chart:', error);
    }
}

// Example usage
fetchTeamProjections().then(projections => {
    generateChart(projections);
});
