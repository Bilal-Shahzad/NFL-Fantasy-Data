const axios = require('axios');
const fs = require('fs');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

async function getSleeperPlayerData() {
    const url = ''; //api goes here

    try {
        const response = await axios.get(url);
        const players = response.data;

        const playerData = Object.values(players).map(player => ({
            player_id: player.player_id,
            first_name: player.first_name,
            last_name: player.last_name,
            position: player.position,
            team: player.team,
            age: player.age,
            fantasy_positions: player.fantasy_positions ? player.fantasy_positions.join(', ') : '',
            years_exp: player.years_exp
        }));

        const csvWriter = createCsvWriter({
            path: 'data/sleeper_player_data.csv',
            header: [
                {id: 'player_id', title: 'Player ID'},
                {id: 'first_name', title: 'First Name'},
                {id: 'last_name', title: 'Last Name'},
                {id: 'position', title: 'Position'},
                {id: 'team', title: 'Team'},
                {id: 'age', title: 'Age'},
                {id: 'fantasy_positions', title: 'Fantasy Positions'},
                {id: 'years_exp', title: 'Years Experience'}
            ]
        });

        if (!fs.existsSync('data')) {
            fs.mkdirSync('data');
        }

        await csvWriter.writeRecords(playerData);
        console.log('Data saved to data/sleeper_player_data.csv');
    } catch (error) {
        console.error('Failed to fetch data:', error);
    }
}

getSleeperPlayerData();
