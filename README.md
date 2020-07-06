# HowMuchTimeHaveIWasted.com
The purpose of this app is to show you how many hours you wasted playing games and if you want to cry even more look at your csgo stats.

## How it works:
- You give it your steam user id. e.g: `76561198066000502` (account has to be public)
- We connect with the steam api and get your user data and your game list. [Steam API docs](https://developer.valvesoftware.com/wiki/Steam_Web_API#Interfaces_and_method)
- Then we calculate the amount of hours you spent in total playing games
- We provide you with an overall rating and score (total_hours x (total_hours * 0.5)).
- Additionally if the user owns and has played csgo we can display cool stats in graphs pie charts diagrams

### Ratings: 
- 0 -> 49 hours: **What even are games?** Seriously what are they???
- 50 -> 299 hours: **You might aswell just play mobile games** Sponsored by RAID: Shadow Legends
- 300 -> 599 hours: **You gotta pump those numbers up. Those are rookie numbers** I myself have more than 1000 hours
- 600 -> 999 hours: **Even my mum has more hours on candy crush** She's over level 9000
- 1000 -> 1999 hours: **Its all civilisation isnt it?** Just one more turn
- 2000 -> 3999 hours: **You have a healthy balance** Not too much but not too little
- 4000 -> 5999 hours: **Are you going pro??** * insert wannabe esports pro starter pack *
- 6000 -> 7999 hours: **Certified Hardcore Gamer** Get your certificate here: [www.ImaHardcoreGamer.com](https://youtu.be/dQw4w9WgXcQ)
- 8000 -> 9999 hours: **Dude. Are you okay?** When was the last time you went outside??
- 10'000 and onwards: **You need to seek medical help** https://www.nhs.uk/

## User Stories:

**As a** user
**I want** I view the total hours I have on my steam account
**So that** the user can see how much of my life I wasted

- **As a** user
**I want** to know which account I accessed 
**So that** I know I am looking at the right account

- **As a** user
**I want** to get a score based on my total hours
**So that** I can compare against other steam users

- **As a** user
**I want** to know if the steam id I entered is incorrect or correct
**So that** I can enter it in correctly and see the statistics

- **As a** user
**I want** to get a rating based on my total hours played
**So that** I can see how bad/good I am at living life

- **As a** user
**I want** to know the reason why it couldn't access my account and how to fix
**So that** I can try and fix it

**As a** user
**I want** to see more statistics about csgo
**So that** I can assert my dominance over other players

- **As a** user
**I want** to see my total hours on csgo
**So that** I can see much of my life I wasted on CSGO

- **As a**
**I want**
**So that**





















## Links:
**Get user:**

- http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamids=76561198066000502

**Get game stats:** 

- http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=76561198066000502

**Get owned game list:**

- http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=76561198066000502&format=json

**Get recently played games:**

- http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=2FA14ED02A1D7CCC0E4FCA80AE6AE194&steamid=76561198066000502&format=json

- We then compare your total hours to a list of activities or great achievments that were done in less time