// This is the file that was converted to discord.py
// Modules so the bot can function
const {Client, GatewayIntentBits} = require('discord.js');
require('dotenv').config();

// Regular expression for URL detection
const urlRegex = /(https?:\/\/[^\s]+)/g;


// Create the client or bot with its intents
const client = new Client({
     intents: [
        GatewayIntentBits.Guilds, 
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers
        ]
});

// Initiate the client with a ready message
Client.once('ready', () =>{
    console.log(`${client.user.tag} is Ready!`)
    client.user.setPresence({
        status: PresenceUpdateStatus.Online,
        activities: [{name: 'Listening', type: ActivityType.Watching}]
    });
});

// Initiate a message listener
Client.on('messageCreate', () => {
    // Ignore messages from bots
    if (message.author.bot) return;
    // Check if the message content contains a URL
    if (urlRegex.test(message.content)) {
    // Notify the owner
    console.log('Hyperlink detected:', message.content)
    // Remove the message containing the hyperlink
    message.delete()
        .then(() => message.reply('I see you posted a link!\nThat\'s not allowed! :D'))
        .catch(console.error);
    }
});

// Login the Client
client.login(process.env.BOT_TOKEN);