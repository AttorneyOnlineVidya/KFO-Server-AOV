from time import gmtime, strftime

import requests
import json
import random

from server import database


class Webhooks:
    """
    Contains functions related to webhooks.
    """

    def __init__(self, server):
        self.server = server

    def send_webhook(
        self,
        username=None,
        avatar_url=None,
        message=None,
        FieldA_1=None,
        FieldA_2=None,
        FieldB_1=None,
        FieldB_2=None,
        embed=False,
        title=None,
        color=None,
        description=None,
        image=None,
        thumbnail=None,
        url=None,
    ):
        is_enabled = self.server.config["webhooks_enabled"]
        if url is None:
            url = self.server.config["webhook_url"]

        if not is_enabled:
            return

        current_time = strftime("%H:%M", gmtime())

        data = {}
        data["content"] = message
        data["avatar_url"] = avatar_url
        data["username"] = username if username is not None else "tsuserver webhook"
        if embed is True:
            data["embeds"] = []
            embed = {}

            embed["fields"] = []  
            embed["fields"].append({"name": FieldA_1, "value": FieldA_2, "inline": True})
            embed["fields"].append({"name": FieldB_1, "value": FieldB_2, "inline": False})


            embed["description"] = description            
            embed["title"] = title

            embed["image"] = {}
            embed["image"].update({"url": image})
            embed["thumbnail"] = {}
            embed["thumbnail"].update({"url": thumbnail})

            embed["footer"] = {}
            embed["footer"].update({"text": "Sent at " + current_time + " UTC"})

            embed['color'] = color
            data["embeds"].append(embed)
        result = requests.post(
            url, data=json.dumps(data), headers={"Content-Type": "application/json"}
        )
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            database.log_misc("webhook.err", data=err.response.status_code)
        else:
            database.log_misc(
                "webhook.ok",
                data="successfully delivered payload, code {}".format(
                    result.status_code
                ),
            )

    def modcall(self, id, char, ipid, area, reason=None):
        is_enabled = self.server.config["modcall_webhook"]["enabled"]
        username = self.server.config["modcall_webhook"]["username"]
        avatar_url = self.server.config["modcall_webhook"]["avatar_url"]
        no_mods_ping = self.server.config["modcall_webhook"]["ping_on_no_mods"]
        mod_role_id = self.server.config["modcall_webhook"]["mod_role_id"]
        mods = len(self.server.client_manager.get_mods())
        color = self.server.config["modcall_webhook"]["color"]

        if not is_enabled:
            return

        if mods == 0 and no_mods_ping:
            modcall = f"<&@{mod_role_id}>"
            message = f"{modcall if mod_role_id is not None else '@here'} A user called for a moderator, but there are none online!"
        else:
            if mods == 1:
                s = ""
            else:
                s = "s"
            message = f"New modcall received ({mods} moderator{s} online)"

        description = f"[{id}] {char} (IPID: {ipid}) in [{area.id}] {area.name}"
        if reason.isspace():
            reason = "No reason given"

        self.send_webhook(
            username=username,
            avatar_url=avatar_url,
            message=message,
            FieldA_1="",
            FieldA_2="",
            FieldB_1="Reason:",
            FieldB_2=reason,
            embed=True,
            title="Modcall",
            color=color,
            description=description,
            image=None,
            thumbnail=None,
            url=self.server.config["modcall_url"]
        )

    def advert(self, char, area, msg=None):
        import re
        is_enabled = self.server.config["advert_webhook"]["enabled"]
        username = self.server.config["advert_webhook"]["username"]
        avatar_url = self.server.config["advert_webhook"]["avatar_url"]
        advert_urls = self.server.config["advert_url"]

        if not is_enabled:
            return
        caseF = True
        titleF = "Advert Title"
        case_title_list = self.server.misc_data['case_advert_titles']
        game_title_list = self.server.misc_data['game_advert_titles']
        ping_list = self.server.misc_data['role_pings']
        player_roles = []

        l_def = ["def", "defense", "defence", "defender", "defs", "defenses", "defences", "defenders"]
        l_pro = ["pro", "prosecution", "prosecutor", "pros", "prosecutions", "prosecutors"]
        l_wit = ["wit", "wits", "witness", "witnesses", "det", "dets", "detective", "detectives", "jury", "jur", "jurs", "juror", "jurors"]
        l_jud = ["jud", "juds", "judge", "jooj", "judges", "joojs"]
        l_steno = ["steno", "stenographer", "stenos", "stenographers"]
        need_keys = l_def + l_pro + l_wit + l_jud + l_steno

        roles = {}
        for key in ["bench", "benches"]: # If /need contains these words
            list = ping_list['def'], ping_list['pro'] # Add those discord roles to the ping list via miscdata
            roles[key] = " ".join(map(str, list))
        for key in l_def:
            roles[key] = ping_list['def']
        for key in l_pro:
            roles[key] = ping_list['pro']
        for key in l_wit:
            roles[key] = ping_list['witdet']
        for key in l_jud:
            roles[key] = ping_list['jud']
        for key in l_steno:
            roles[key] = ping_list['steno']

        all_roles = ping_list['def'], ping_list['pro'], ping_list['witdet'], ping_list['jud'], ping_list['steno']
        all_pings = " ".join(map(str, filter(None, all_roles)))

        pings = []
        check = msg.lower()
        recheck = re.split('\W+', check)
        if "Arcade" in area.name:
            pings.append(ping_list["arcade"])
            caseF = False
        elif "all roles" in check:
            pings.append(all_pings)
            player_roles = ["Defense", "Prosecution", "Witnesses", "Judge", "Steno"]
            players = ", ".join(player_roles)
        else:
            for x in recheck:
                if x in roles and roles[x] not in pings:
                    pings.append(roles[x]) # add pings
                if x in need_keys:
                    player_roles.append(x.capitalize()) # add non-ping to embed
            noDupe = tuple(dict.fromkeys(player_roles)) # avoid duplicate roles
            players = ", ".join(noDupe)

        if caseF:
            titleF = "🚨 Case Advert 🚨"
            color = self.server.config["advert_webhook"]["case_color"]
            message = f"{random.choice(case_title_list)}\n"
            thumbnail = random.choice(self.server.config["advert_webhook"]["case_img"])
            if not player_roles:
                players = "None"
        else:
            titleF = "🚨 Game Advert 🚨"
            color = self.server.config["advert_webhook"]["game_color"]
            message = f"{random.choice(game_title_list)}\n"
            thumbnail = random.choice(self.server.config["advert_webhook"]["game_img"])
            players = "Players"
        
        #message += " ".join(filter(None, pings))
        ping_message = " ".join(filter(None, pings)) #add pings to discord message
        full_message = message + ping_message

        description = f"**{char}** {'needs people for a case!' if msg is None else f'needs {msg[:256]}'}"

        for index, link in enumerate(advert_urls):
            self.send_webhook(
                username=username,
                avatar_url=avatar_url,
                message=full_message if index == 0 else message, #only add pings to the first URL in the list to avoid unknown-role error
                FieldA_1="Area:",
                FieldA_2=area.name,
                FieldB_1="Roles needed:",
                FieldB_2=players,
                embed=True,
                title=titleF,
                color=color,
                description=description,
                image=None,
                thumbnail=thumbnail,
                url=link
            )


    def kick(self, ipid, hdid, reason="", client=None, char=None):
        is_enabled = self.server.config["kick_webhook"]["enabled"]
        username = self.server.config["kick_webhook"]["username"]
        avatar_url = self.server.config["kick_webhook"]["avatar_url"]

        if not is_enabled:
            return

        message = f"{char} (IPID: {ipid}, HDID: {hdid})" if char is not None else str(ipid)
        message += " was kicked"
        message += (
            f" by {client.name} ({client.ipid})"
            if client is not None
            else " from the server"
        )
        message += (
            f" with reason: {reason}"
            if reason.strip() != ""
            else " (no reason provided)."
        )

        self.send_webhook(username=username,
                          avatar_url=avatar_url, message=message)

    def ban(
        self,
        ipid,
        hdid,
        ban_id,
        hdban,
        reason="",
        length="",
        client=None,
        char=None,
        unban_date=None,
    ):
        is_enabled = self.server.config["ban_webhook"]["enabled"]
        username = self.server.config["ban_webhook"]["username"]
        avatar_url = self.server.config["ban_webhook"]["avatar_url"]
        if unban_date is not None:
            unban_date = unban_date.strftime("%Y-%m-%d %H:%M:%S %Z")

        if not is_enabled:
            return
        message = f"{char} (IPID: {ipid}, HDID: {hdid})" if char is not None else str(ipid)
        message += (
            f" was hardware-banned"
            if hdban
            else " was banned"
        )
        message += f" for {length}"
        message += (
            f" by {client.name} ({client.ipid})"
            if client is not None
            else " from the server"
        )
        message += f" with reason: {reason}" if reason.strip() != "" else ""
        message += f" (Ban ID: {ban_id}).\n"
        message += (
            f"It will expire {unban_date}"
            if unban_date is not None
            else "It is a permanent ban."
        )

        self.send_webhook(username=username,
                          avatar_url=avatar_url, message=message)

    def unban(self, ban_id, client=None):
        is_enabled = self.server.config["unban_webhook"]["enabled"]
        username = self.server.config["unban_webhook"]["username"]
        avatar_url = self.server.config["unban_webhook"]["avatar_url"]

        if not is_enabled:
            return

        message = f"Ban ID {ban_id} was revoked"
        message += (
            f" by {client.name} ({client.ipid})."
            if client is not None
            else " by the server."
        )

        self.send_webhook(username=username,
                          avatar_url=avatar_url, message=message)
        
    def warn(self, ipid, hdid, reason="", client=None, char=None):
        is_enabled = self.server.config["warn_webhook"]["enabled"]
        username = self.server.config["warn_webhook"]["username"]
        avatar_url = self.server.config["warn_webhook"]["avatar_url"]

        if not is_enabled:
            return

        message = f"{char} (IPID: {ipid}, HDID: {hdid})" if char is not None else str(ipid)
        message += " was warned"
        message += (
            f" by {client.name} ({client.ipid})"
            if client is not None
            else " from the server"
        )
        message += (
            f" with reason: {reason}"
            if reason.strip() != ""
            else " (no reason provided)."
        )

        self.send_webhook(username=username,
                          avatar_url=avatar_url, message=message)
