import fetch from 'node-fetch';  // Use import statement for ES modules

const leagueId = '1125151990448902144';
const teamId = 'Bilshaz';

async function getSleeperData() {
    try {
        // Fetch league data
        const leagueResponse = await fetch(`https://api.sleeper.app/v1/league/${leagueId}`);
        const leagueData = await leagueResponse.json();

        // Fetch team data
        const teamResponse = await fetch(`https://api.sleeper.app/v1/team/${teamId}`);
        const teamData = await teamResponse.json();

        console.log('League Data:', leagueData);
        console.log('Team Data:', teamData);

        // Process and return the data as needed
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

getSleeperData();
