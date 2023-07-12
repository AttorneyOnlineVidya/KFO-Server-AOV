# KFO-Server-AOV
**Attorney Online Vidya’s** server code has been updated from _tsuserver3_ to _KFO-Server_, the new standard for python based Attorney Online servers.
While most features remain the same between code bases, there are several changes and new features that we have documented below to help you use them, as well as general differences between KFO-Server base and our own server.
<br>**Note that several of these features may require CM.**

If you encounter any issues or bugs, please contact AOV staff via server Mod Call or our Discord.

## General AOV Changes From KFO-Base / tsuserver3
* **Minigames and Cutscenes**
	- The main new features of KFO-Server, as highlighted and documented below.
	- Minigames replicate mechanics from Danganronpa games, but can likely be used in another context.
	- Cutscenes (or "Demos") can now be created and played on server. See below for more instructions.
* **Other Functionality and Improvements**
	- Various other new or improved commands are listed below. For a full command list, check [here](https://github.com/AttorneyOnlineVidya/KFO-Server-AOV/blob/master/docs/commands.md)
		- Note that not all commands in the above link will be available on AOV, either because they're redundant or not appropriate.
* **Hub System Disabled**
	- The concept of having multiple hubs with a separate collection of areas. Unnecessary for AOV and generally turned off, so don't worry about it.
* **DJ and Looping Music**
	- DJ is dead. `/play` now loops by default. Use `/play1` if you want to play a song only once.
* **Discord Webhooks**
	- Case Adverts and Mod Calls are now simultaneously posted to relevant channels in AOV Discords.
		- For Case Adverts, check [below](https://github.com/AttorneyOnlineVidya/KFO-Server-AOV/blob/master/docs/KFO-Server-AOV%20Guide.md#case-advert-webhook) for usage information. 
		- If no Mods are online, the Mod Call webhook will alert them and a mod will log in ASAP.
			- Obviously, abuse of these will get your ass banned.

# New Server Features
## Minigames
**Note: These can only be activated if the area's evidence_mod is set to "CT" as they are otherwise disruptive. Ask a mod for help.**
* **cs** `<id>`
    - Start a one-on-one "Cross Swords" debate with targeted player!
    - Will automatically pair you with the target
    - Starts an area timer for 5 minutes.
    - If there's an ongoing cross-swords already, it will turn into a Scrum Debate (team vs team debate) with you joining the side *against* the `<id>`.
* **pta** `<id>`
    - Start a one-on-one "Panic Talk Action" debate with targeted player!
    - Unlike `/cs`, a Panic Talk Action (PTA) cannot evolve into a Scrum Debate, thus is more for 1-on-1 purposes.
    - Starts an area timer for 5 minutes.
* **concede** `<id>`
    - Concede a trial minigame and withdraw from either team you're part of or end the minigame.
## Demo / Cutscenes
* **demo** `[evidence id]`
	- "Cutscenes", officially called 'Demos', can be created and played using demo files and evidence.
	- The easiest way to do this is to turn 'Log To Demo Files' on in your client's Settings > Logging options.
	- Then, on server, play out your cutscene using your preferred characters, effects and general actions. A date and time-stamped demo file is created in your client's "logs" folder in a folder named after the server once you connect:<br>
	![Demo File Location](https://cdn.discordapp.com/attachments/657301457086840837/1096399796786434068/demoFileLocation.png)
	- Open the demo file in a text editor such as Notepad++. From here you can scroll down to see the individual lines relating to each action you performed. It will look like this:<br>
	![A Demo File open in Notepad++](https://cdn.discordapp.com/attachments/657301457086840837/1096402000763170886/demoFile.png)
	- These lines basically consist of client commands involving talking IC, animations, backgrounds and effects. 
		- You can edit and manipulate these as needed. For example, you can delete the unnecessary initial top-line character list, modify any wait times, change backgrounds with "BN#" and edit "MS#" (IC Chat) lines to include or change SFX or visual effects. 
	- Once edited down to your preference, copy and paste these lines into the Description of a piece of evidence. Note the following:
		- If playing music, any line starting with "MC#" must be replaced with `/play` to play music instead. Other commands can be used as well.
		- You must use `%` to end a line. 
		- Evidence desciptions have a character limit. As such, you can chain to another demo evidence by putting `/demo [next evidence id]` as the last line to continue the full demo.
	- Here is an example of what this should look like:<br> 
	![Demo Evidence Text Example](https://cdn.discordapp.com/attachments/657301457086840837/1096387674887163964/demoFileExample.png)
	- When finished, use `/demo [evidence name or ID]` to play the cutscene. Use `/demo` by itself to stop it.
## Case Advert Webhook
* **need** `message`
	- Sending an advert through `/need` will automatically post it to the AOV Community Server's #Case-Advertising channel.
	- This will also include your current area as well as pinging any roles mentioned in the advert.
		- Role pings that can be included are Defense, Prosecution, Judge, Witness/Detective (also includes Jury roles) and Stenographer. Shorter versions, such as "def" or "steno" are also recognised.
	- eg. "/need defense, co-pro, and steno for case!" will ping the Discord's Defense, Prosecution and Stenographer roles.
	- Putting "All roles" in the message will ping all roles.
	- The 'Arcade' role will be pinged automatically if a `/need` is sent from an Arcade-named area.
## Testimony Commands
**Note: Testimony recording can also be used from IC Chat as a CM - see "In-Character Commands" below.**
* **testimony** `[id]`
    - Display the currently recorded testimony, including statement IDs.
    - Optionally, `id` is a nubmer that can be passed to move to that statement ID.
* **testimony\_start** `<title>`
    - Manually start a testimony with the given title.
* **testimony\_continue**
    - Manually start a testimony with the given title.
* **testimony\_clear**
    - Clear the current testimony.
* **testimony\_remove** `<id>`
    - Remove the statement at index.
* **testimony\_amend** `<id>` `<msg>`
    - Edit the spoken message of the statement at idx.
* **testimony\_swap** `<id>` `<id>`
    - Swap the two statements by id.
* **testimony\_insert** `<id>` `<id>`
    - Insert the targeted statement at idx.
## In-Character Chat Commands
* **/a** `[id(s)]` `[msg]`
    - Put this in the In-Character chat. Use to message other areas you are a CM in.
    - This command can only be used by CMs and above.
    - `[id(s)]` are optional. If ID(s) are not provided (`/a msg`), the message will be broadcast across all owned areas.
    - `[id(s)]` stand for Area ID's that can be viewed using `/area`, or in the A/M area list, so `/a 1 msg` to send message "msg" to area ID 1. If multiple ID's, they must be comma-separated, like so: `/a 1,2,3,4 msg` - send message "msg" to area ID's 1, 2, 3 and 4.
* **/w** `[id(s)]` `[msg]`
    - Put this in the In-Character chat. Used to whisper to other players.
    - This command can be used by anyone, unless `/area_pref can_whisper` is `false`.
    - `[id(s)]` are optional. If ID(s) are not provided (`/w msg`), the message will be broadcast to clients in the current `/pos` only.
    - `[id(s)]` stand for Client ID's that can be viewed using `/getarea`, so `/w 1 msg` to send message "msg" to client with ID 1. The client must be present in the same area. If multiple ID's, they must be comma-separated, like so: `/aw 1,2,3,4 msg` - send message "msg" to Client ID's 1, 2, 3 and 4.
* **Testimony**
    - Begin with a title, like `--title--`, `==title==`, etc.
    - When a CM presses the "Witness Testimony" button, any message spoken from this point on will be recorded.
        - If anyone that isn't a CM tries to do this, it will not start recording. Use the OOC `/testimony` commands detailed above instead.
    - Once everyone has testified, last one to testify or the CM has to say a single word - `end` to finish recording.
    - Afterwards, next time the CM uses "Cross-Examination" button, the testimony title will be replayed, and the defense can use `>` to progress a statement, `<` to precede a statement, `>5` to go to specific statement 5.
    - You can use `**msg` to amend the current statement.
    - You can use `++msg` to add a new statement after the current one.
## Areas
* **desc** `[desc]`
    - Set an area description that appears to the user any time they enter the area.
		- Could be used to immediately detail the current case format and summary to incoming users.
* **edit\_ambience** `[tog]`
    - Toggle edit mode for setting ambience.
    - Playing music with this on will then set it as the area's 'ambience', playing as SFX rather than music effectively allowing for background tracks.
* **lights** `[tog]`
    - Toggle lights for this area. If lights are off, players will not be able to use `/getarea` or see evidence.
    - You can change `/bg`, `/desc` and `/pos_lock` of the area when its dark and it will remember it next time you turn the lights off.
    - tog can be `on`, `off` or empty.
* **follow**
    - Follow targeted character ID if they move area.
* **unfollow**
    - Stop following whoever you are following.
## Casing
**Various evidence features can now be used through OOC commands if preferred, as detailed below.**
* **evidence** `[evi_name/id]`
    - Use `/evidence` to read all evidence in the area.
    - Use `/evidence` `[evi_name/id]` to read specific evidence.
* **evidence_add** `[name]` `[desc]` `[image]`
    - Add a piece of evidence.
    - For sentences with spaces the arg should be surrounded in `""`'s, for example `/evidence_add Chair "It's a chair." chair.png`
* **evidence_remove** `<evi_name/id>`
    - Remove a piece of evidence.
* **evidence_edit** `<evi_name/id>` `[name]` `[desc]` `[image]`
    - Edit a piece of evidence.
    - If you don't want to change something, put an `*` there.
    - For sentences with spaces the arg should be surrounded in `""`'s, for example `/evidence_edit * "It's a chair." chair.png`
* **evi\_swap**  `<id>` `<id>`
    - Swap the positions of two evidence items on the evidence list.
    - The ID of each evidence can be displayed by mousing over it in 2.8 client, or simply its number starting from 1.
* **remote\_listen** `[option]`
    - Change the remote listen logs to either `NONE`, `IC`, `OOC` or `ALL`.
    - It will send you those messages from the areas you are an owner of.
    - Leave blank to see your current option.
## Character
* **player\_move\_delay** `<id>` `[delay]`
    - Set the player's move delay to a value in seconds. Can be negative.
    - Delay must be from `-1800` to `1800` in seconds or empty to check.
    - If only `delay` is provided, you will be setting your own move delay.
* **player\_hide** `<id(s)>`
    - Hide player(s) from `/getarea` and playercounts.
    - If `<id>` is `*`, it will hide everyone in the area excluding yourself and CMs.
* **player\_unhide** `<id(s)>`
    - Unhide player(s) from `/getarea` and playercounts.
    - If `<id>` is `*`, it will unhide everyone in the area excluding yourself and CMs.
* **hide** `<evi_name/id>`
    - Try to hide in the targeted evidence name or ID.
* **unhide**
    - Stop hiding.
* **listen\_pos** `[pos(s)]`
    - Start only listening to your currently occupied pos.
    - All messages outside of that pos will be reflected in the OOC.
    - Optional argument(s) is a list of positions you want to listen to.
* **unlisten\_pos**
    - Undo the effects of `/listen_pos` command so you stop listening to the position(s).
* **chardesc** `[desc/id]`
    - Look at your own character description if no arugments are provided.
    - Look at another person's character description if only ID is provided.
    - Set your own character description if description is provided instead of ID.
        - Do note that the first sentence of your chardesc is displayed during area transfer messages!
    - To set someone else's char desc as an admin/GM, or look at their desc, use `/chardesc_set` or `/chardesc_get`.
* **chardesc\_set** `<id>` `[desc]`
    - Set someone else's character description to desc or clear it.
* **chardesc\_get** `<id>`
    - Get someone else's character description.
* **narrate** `[on|off]`
    - Speak as a Narrator for your next emote, speaking over the current IC visuals.
## Music
* **play** `<name>`
    - `/play` now loops a track by default, otherwise works as normal.
* **play1** `<name>`
    - If you only want to play a track once rather than loop, use this.
* **musiclists**
    - Displays all the available music lists in server storage.
* **musiclist** `[path]`
    - Load a music list from server storage that only you will see. Pass no arguments to reset. `/musiclists` to see available lists.
* **area\_musiclist** `[path]`
    - Load a music list from server storage that can be seen by the whole area. Pass no arguments to reset. `/musiclists` to see available lists.
    - Area list takes priority over client lists.
* **random\_music** `[category]`
    - Play a random track from your current muisc list. If supplied, `[category]` will pick the song from that category.
    - Usage: `/random_music [category]`
## Roleplay
* **Standard Actions**
	- `/roll, /notecard, /coinflip, /8ball` all work as standard, with some minor additions outlined below:
* **notecard** `<message>`
    - Write a notecard that can only be revealed by a CM.
* **notecard\_clear**
    - Clear all notecards as a CM.
* **notecard\_reveal**
    - Reveal all notecards and their owners.
* **notecard\_check**
    - Check all notecards and their owners privately with a message telling others you've done so.
* **vote** `<id>`
    - Cast a vote for a particular user that can only be revealed by a CM.
* **vote\_clear** `[char_folder]`
    - Clear all votes as a CM.
    - Include `[char_folder]` (case-sensitive) to only clear a specific voter.
* **vote\_reveal**
    - Reveal the number of votes, the voters and those with the highest amount of votes.
* **vote\_check**
    - Check the number of votes, the voters and those with the highest amount of votes privately with a message telling others you've done so.
* **timer** `<id> [+/-][time]` OR `<id> start` OR `<id> <pause|stop>` OR `<id> <unset|hide>`
    - Manage a countdown timer in the current area. Note that timer of ID `0` is hub-wide. All other timer ID's are local to area.
    - Anyone can check ongoing timers, their status and time left using `/timer <id>`, so `/timer 0`.
    - `[time]` can be formated as `10m5s` for 10 minutes 5 seconds, `1h30m` for 1 hour 30 minutes, etc.
    - You can optionally add or subtract time, like so: `/timer 0 +5s` to add `5` seconds to timer id `0`.
    - `start` starts the previously set timer, so `/timer 0 start`.
    - `pause` OR `stop` pauses the timer that's currently running, so `/timer 0 pause`.
    - `unset` OR `hide` hides the timer for it to no longer show up, so `/timer 0 hide`.
