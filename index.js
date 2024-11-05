import dotenv from 'dotenv';
import schedule from 'node-schedule';

dotenv.config();

import { Client, GatewayIntentBits, ActionRowBuilder, ButtonBuilder, ButtonStyle, Events } from 'discord.js';

const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.DirectMessage, GatewayIntentBits.GuildMembers],
});

client.login(process.env.DISCORD_TOKEN);

const trashChannelId = '1303271594881454143';

const users = ['leocia', '.tanguita1', 'katodiaz'];

const taskDates = [
    new Date('2024-11-05T12:45:00'), // Example date 1
];


let last_user_index = 0;

import { Client, GatewayIntentBits, ActionRowBuilder, ButtonBuilder, ButtonStyle, Events } from 'discord.js';

// In the task scheduling section, send a message with a button
taskDates.forEach((date) => {
    schedule.scheduleJob(date, async () => {
        taskCompleted = false;
        const userToPing = selectNextUser(users);
        const channel = await client.channels.fetch(trashChannelId);

        // Create a "Mark as Done" button
        const row = new ActionRowBuilder()
            .addComponents(
                new ButtonBuilder()
                    .setCustomId('mark_done')
                    .setLabel('Ya saque la basura ctm')
                    .setStyle(ButtonStyle.Success)
            );

        await channel.send({
            content: `@${userToPing}, mamabishoo saca la basura pi.`,
            components: [row],
        });

        setReminder(channel, userToPing);
    });
});

// Event listener for button interactions
client.on(Events.InteractionCreate, async (interaction) => {
    if (!interaction.isButton()) return;

    if (interaction.customId === 'mark_done') {
        taskCompleted = true;
        await interaction.reply({ content: `Buena crack, @${interaction.user.username}! hiciste algo (eso ya es mas de lo que harchi hizo este mes).`, ephemeral: true });
    }
});

function selectNextUser(userIds) {
    return userIds[last_user_index++ % userIds.length];
}

client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});
