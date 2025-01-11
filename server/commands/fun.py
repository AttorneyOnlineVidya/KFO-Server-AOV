from server import database
from server.constants import TargetType
from server.exceptions import ClientError, ArgumentError

from . import mod_only

__all__ = [
    "ooc_cmd_disemvowel",
    "ooc_cmd_undisemvowel",
    "ooc_cmd_shake",
    "ooc_cmd_unshake",
    "ooc_cmd_gimp",
    "ooc_cmd_ungimp",
    "ooc_cmd_washhands",
    "ooc_cmd_rainbow",
    "ooc_cmd_emoji",
    "ooc_cmd_aussie",
    "ooc_cmd_tag",
    "ooc_cmd_vote",
    "ooc_cmd_polls",
    "ooc_cmd_polladd",
    "ooc_cmd_pollremove",
    "ooc_cmd_polldetail",
    "ooc_cmd_pollchoiceclear",
    "ooc_cmd_pollchoiceremove",
    "ooc_cmd_pollchoiceadd",
]


@mod_only()
def ooc_cmd_disemvowel(client, arg):
    """
    Remove all vowels from a user's IC chat.
    Usage: /disemvowel <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except Exception:
        raise ArgumentError("You must specify a target. Use /disemvowel <id>.")
    if targets:
        for c in targets:
            database.log_area("disemvowel", client, client.area, target=c)
            c.disemvowel = True
        client.send_ooc(f"Disemvowelled {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")


@mod_only()
def ooc_cmd_undisemvowel(client, arg):
    """
    Give back the freedom of vowels to a user.
    Usage: /undisemvowel <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except Exception:
        raise ArgumentError(
            "You must specify a target. Use /undisemvowel <id>.")
    if targets:
        for c in targets:
            database.log_area("undisemvowel", client, client.area, target=c)
            c.disemvowel = False
        client.send_ooc(f"Undisemvowelled {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")


@mod_only()
def ooc_cmd_shake(client, arg):
    """
    Scramble the words in a user's IC chat.
    Usage: /shake <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except Exception:
        raise ArgumentError("You must specify a target. Use /shake <id>.")
    if targets:
        for c in targets:
            database.log_area("shake", client, client.area, target=c)
            c.shaken = True
        client.send_ooc(f"Shook {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")


@mod_only()
def ooc_cmd_unshake(client, arg):
    """
    Give back the freedom of coherent grammar to a user.
    Usage: /unshake <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except Exception:
        raise ArgumentError("You must specify a target. Use /unshake <id>.")
    if targets:
        for c in targets:
            database.log_area("unshake", client, client.area, target=c)
            c.shaken = False
        client.send_ooc(f"Unshook {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")


@mod_only()
def ooc_cmd_gimp(client, arg):
    """
    Replace a user's message with a random message from a list.
    Usage: /gimp <id>
    """
    if len(arg) == 0:
        raise ArgumentError('You must specify a target ID.')
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False)
    except Exception:
        raise ArgumentError('You must specify a target. Use /gimp <id>.')
    if targets:
        for c in targets:
            database.log_misc('gimp', client, target=c, data=client.area.abbreviation)
            c.gimp = True
        client.send_ooc(f'Gimped {len(targets)} existing client(s).')
    else:
        client.send_ooc('No targets found.')

@mod_only()
def ooc_cmd_ungimp(client, arg):
    """
    Allow the user to send their own messages again.
    Usage: /ungimp <id>
    """
    if len(arg) == 0:
        raise ArgumentError('You must specify a target ID.')
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False)
    except Exception:
        raise ArgumentError('You must specify a target. Use /ungimp <id>.')
    if targets:
        for c in targets:
            database.log_misc('ungimp', client, target=c, data=client.area.abbreviation)
            c.gimp = False
        client.send_ooc(f'Ungimped {len(targets)} existing client(s).')
    else:
        client.send_ooc('No targets found.')


def ooc_cmd_washhands(client, arg):
    """
    Stay safe!
    Usage: /washhands
    """
    client.send_ooc('You washed your hands!')


def ooc_cmd_rainbow(client, arg):
    """
    Activate or Deactivate rainbow text.
    Usage: /rainbow
    """
    if client.rainbow:
        client.rainbow = False
        client.send_ooc("Rainbow Mode DEACTIVATED.")
    else:
        client.rainbow = True
        client.send_ooc(f"Rainbow Mode ACTIVATED.")

gokudrip = """
wait#280#%
BN#OCCourtSky#%
/play1 https://cdn.discordapp.com/attachments/657301457086840837/1090753556237266954/Official_Goku_Drip_Theme_-_Ultra_Dripstinct.mp3 %
MS#1#-#Phoenix#confident# #def#1#0#0#0#0#0#0#0#0#Phoenix#-1###0<and>0#0#0#0#0#0#-^(b)confident^(a)confident^#-^(b)confident^(a)confident^#-^(b)confident^(a)confident^#0#dbzteleport||dbz-teleport#%
wait#2500#%
BN#OCCourtSky#%
MS#1#hat#Hershel#hat# #pro#1#0#6#0#0#0#1#0#0#Layton#-1###0<and>0#0#0#0#0#0#hat^(b)hat^(a)hat^#hat^(b)hat^(a)hat^#hat^(b)hat^(a)hat^#0#dbzteleport||dbz-teleport#%
wait#2300#%
BN#OCCourtSky#%
MS#1#-#Phoenix_SOJ_Wit#stern# #jud#1#0#0#0#0#0#0#0#0#Phoenix?#-1###0<and>0#0#0#0#0#0#-^(b)stern^(a)stern^#-^(b)stern^(a)stern^#-^(b)stern^(a)stern^#0#dbzteleport||dbz-teleport#%
wait#2300#%
BN#OCCourtSky#%
MS#1#mladytipper#Hershel_Pro#mlady# #wit#1#0#6#0#0#0#0#0#0#Layton?#-1###0<and>0#0#0#0#0#0#mladytipper^(b)mlady^(a)mlady^#mladytipper^(b)mlady^(a)mlady^#mladytipper^(b)mlady^(a)mlady^#0#dbzteleport||dbz-teleport#%
wait#2500#%
BN#OCWhiteRoom#%
MS#0#puzzlewin-layton-pre#Phoenix_PLvsAA#puzzlewin-layton#~~}}}By any means necessary. By any means necessary. By any means necessary. By any means necessary. By any means necessary.#def#1#0#0#1#0#0#0#0#0#HYPEBEAST PHOENIX AND LAYTON#-1###0<and>0#0#0#0#0#0#puzzlewin-layton-pre^(b)puzzlewin-layton^(a)puzzlewin-layton^#puzzlewin-layton-pre^(b)puzzlewin-layton^(a)puzzlewin-layton^#puzzlewin-layton-pre^(b)puzzlewin-layton^(a)puzzlewin-layton^#0#slash||sfx-slash#%
"""

def ooc_cmd_emoji(client, arg):
    """
    Activate or Deactivate emoji mode.
    Usage: /emoji
    """
    if client.emoji:
        client.emoji = False
        client.send_ooc("Emoji Mode DEACTIVATED.")
    else:
        client.emoji = True
        client.send_ooc("Emoji Mode ACTIVATED.")

@mod_only()
def ooc_cmd_dank(client, arg):
    """
    Activate or Deactivate full dank mode for the area.
    Warning: this is an absolute God-defying clusterfuck of a mess.
    Usage: /dank
    """
    from server import commands
    targets = [c for c in client.area.clients]
    ann = "bussin"

    for c in targets:
        if not c.emoji:
            c.emoji = True
        if c.dank:
            c.dank = False
            c.emoji = False
        else:
            c.dank = True

    if client.dank:
        ann = f"AREA {client.area.id} DRIP STATUS:\nGOATED WITH THE SAUCE"
        client.area.name = "HYPERBOLIC SWAG CHAMBER"
        client.area.status = "DRIPPED OUT OF THEIR MINDS\n"
        client.area.background = "OCCourtInverted"
        client.area.area_manager.broadcast_area_list()
        client.area.evi_list.add_evidence(client, "Goku's Drip", 
                                          gokudrip, 
                                          "JFAMoney.png", "all")      
        client.area.broadcast_evidence_list()
        commands.call(client, "demo", "Goku's Drip")
        for c in targets:
            c.used_showname_command = True
            c.showname = f"HYPEBEAST-{c.char_name.upper()}"      
        client.send_ooc("Dank Mode ACTIVATED.")
    else:
        ann = f"AREA {client.area.id} DRIP STATUS:\nNONE, COMPLETELY DRY"
        client.area.name = client.area.o_name
        client.area.status = "IDLE"
        client.area.background = client.area.o_background
        client.area.area_manager.broadcast_area_list()
        client.area.play_music("[Misc] Record Scratch", "0", 0, "Reality", 0)
        commands.call(client, "evidence_remove", "Goku's Drip")
        client.area.broadcast_evidence_list()
        client.area.stop_demo()
        for c in targets:
            c.used_showname_command = False
            c.showname = ""     
        client.send_ooc(f"Dank Mode DEACTIVATED.")

    client.server.send_all_cmd_pred(
        "CT",
        client.server.config["hostname"],
        f"==== ALERT ====\r\n{ann}\r\n=================",
        "1",
    )

#April
def ooc_cmd_aussie(client, arg):
    """
    Go down under.
    Usage: /aussie
    """
    if arg == "*":
        if client.is_mod:
            targets = [c for c in client.area.clients]
            for c in targets:
                if c.aussie:
                    c.aussie = False
                    c.send_ooc("OI OI OI!")
                else:
                    c.aussie = True
                    c.send_ooc("AUSSIE AUSSIE AUSSIE!")
        else:
            client.send_ooc("Bugger off.")
    else:
        if client.aussie:
            client.aussie = False
            client.send_ooc("OI OI OI!")
        else:
            client.aussie = True
            client.send_ooc("AUSSIE AUSSIE AUSSIE!")


#def ooc_cmd_bp(client, arg):
#    """
#    Show your Bird Level progress.
#    Usage: /bp
#    """
#    client.send_ooc(f'BIRD LEVEL: {client.BPlevel}')
#    client.send_ooc('PROGRESS: ' + '▓'*client.BPprogress + '░'*(client.BPding - client.BPprogress))

        
def ooc_cmd_tag(client, arg):
    """
    Tag someone.
    /tag [id]
    """
    if not client.tag:
        raise ArgumentError('You cannot tag someone if you are not It!')
    if len(arg) == 0:
        raise ArgumentError('You must specify a target ID.')
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False)
    except Exception:
        raise ArgumentError('You must specify a target. Use /tag <id>.')
    if targets:
        for c in targets:
            if c.id == client.id:
                raise ArgumentError('You cannot tag yourself, dumbass.')
            elif c.tag:
                client.send_ooc(f'{c.char_name} is already It!')
            else:
                c.tag = True
                c.send_ooc(f"{client.char_name} tagged you! You're It!")
                client.send_ooc(f'You tagged {c.char_name}! You are no longer It!')
                client.tag = False
    else:
        client.send_ooc('No targets found.')

# Voting system port
def ooc_cmd_vote(client, arg):
    """
    Enter voting mode and vote on a current server poll.
    Usage: /vote
    """
    if not client.hdid.startswith("S-"):
        client.send_ooc("WebAO users are blocked from voting on server polls. Download the client at https://aovidya.pw/AOV")
        return
    if len(arg) == 0:
        polls = client.server.serverpoll_manager.show_poll_list()
        if not polls:
            client.send_ooc('There are currently no polls to vote for.')
        else:
            client.send_ooc('=== Entering Voting Mode... ===')
            message = 'Current polls:'
            for x, poll in enumerate(polls):
                message += '\n{}. {}'.format(x + 1, poll)
            message += '\nEnter the number of the poll in which you would like to vote in. Enter 0 to cancel.'
            client.send_ooc(message)
            client.voting += 1
    else:
        client.send_ooc('This command doesn\'t take arguments')


def ooc_cmd_polls(client, arg):
    """
    See the current list of server polls.
    Usage: /polls
    """
    if len(arg) > 0:
        client.send_ooc('This command doesn\'t take arguments')
    else:
        polls = client.server.serverpoll_manager.show_poll_list()
        if not polls:
            client.send_ooc('There are currently no polls.')
        else:
            message = 'Current server polls:'
            for x, poll in enumerate(polls):
                message += '\n{}. {}'.format(x + 1, poll)
            client.send_ooc(message)

@mod_only()
def ooc_cmd_polladd(client, arg):
    """
    Add a new server poll. Choice defaults are Yes and No.
    Usage: /polladd <Poll Name>
    """
    if client.is_mod:
        if len(arg) <= 1:
            raise ArgumentError("Invalid Argument: Your poll question is too short. Please enter at least more than one character.")
        sarg = arg.replace(" ", "")
        if not sarg.isalnum():
            raise ArgumentError("Invalid Argument: Please do not use special characters (e.g. !#%&?) in your poll question.")
        else:
            client.server.serverpoll_manager.add_poll(arg)
            client.send_ooc('Added {} as a poll.'.format(arg))
            database.log_misc('poll added', client, target=None, data=arg)
    else:
        return

@mod_only()
def ooc_cmd_pollremove(client, arg):
    """
    Remove a server poll.
    Usage: /pollremove <Poll Name>
    """
    if client.is_mod:
        client.server.serverpoll_manager.remove_poll(arg)
        client.send_ooc('Removed {} as a poll.'.format(arg))
        database.log_misc('poll removed', client, target=None, data=arg)
    else:
        return

@mod_only()
def ooc_cmd_polldetail(client, arg):
    """
    Add further details and information to a current server poll.
    Usage: /polldetail <Poll Name>: <Details>
    """
    if client.is_mod:
        if len(arg) == 0:
            client.send_ooc('Command must have an argument!')
        else:
            args = arg.split()
            poll = 1
            for word in args:
                if word.lower().endswith(':'):
                    break
                else:
                    poll += 1
            if poll == len(args):
                raise ArgumentError(
                    'Invalid syntax. Add \':\' in the end of pollname. \n \'/addpolldetail <poll name>: <detail>\'')
            poll_name = ' '.join(args[:poll])
            poll_name = poll_name[:len(poll_name) - 1]
            detail = ' '.join(args[poll:])
            if not detail:
                raise ArgumentError(
                    'Invalid syntax. Expected message after \':\'. \n \'/addpolldetail <poll name>: <detail>\'')
            x = client.server.serverpoll_manager.polldetail(poll_name, detail)
            if x == 1:
                client.send_ooc('Added "{}" as details in poll "{}"'.format(detail, poll_name))
                database.log_misc('poll detail', client, target=None, data=arg)
            else:
                client.send_ooc('Poll does not exist!')
    else:
        return

@mod_only()
def ooc_cmd_pollchoiceclear(client, arg):
    """
    Clear all choices from a server poll.
    Usage: /pollchoiceclear <Poll Name>
    """
    if client.is_mod:
        client.server.serverpoll_manager.clear_poll_choice(arg)
        client.send_ooc('Poll {} choices cleared.'.format(arg))
        database.log_misc('poll choice clear', client, target=None, data=arg)
    else:
        return

@mod_only()
def ooc_cmd_pollchoiceremove(client, arg):
    """
    Clear a specific choice from a server poll.
    Usage: /pollchoiceremove <Poll Name>: <Choice>
    """
    if client.is_mod:
        args = arg.split()
        ooc_name = 1
        for word in args:
            if word.lower().endswith(':'):
                break
            else:
                ooc_name += 1
        if ooc_name == len(args) + 1:
            raise ArgumentError('Invalid syntax. Add \':\' in the end of target.')
        poll = ' '.join(args[:ooc_name])
        poll = poll[:len(poll) - 1]
        choice = ' '.join(args[ooc_name:])
        if not choice:
            raise ArgumentError('Not enough arguments. Use /pollchoiceremove <poll>: <choice to be removed>.')
        x = client.server.serverpoll_manager.remove_poll_choice(client, poll, choice)
        if x is None:
            return
        client.send_ooc(
            'Removed {} as a choice in poll {}. Current choices:\n{} '.format(choice, poll, "\n".join(x)))
        database.log_misc('poll choice removed', client, target=None, data=poll + choice)
    else:
        return

@mod_only()
def ooc_cmd_pollchoiceadd(client, arg):
    """
    Add a choice to a server poll.
    Usage: /pollchoiceadd <Poll Name>: <Choice>
    """
    if client.is_mod:
        args = arg.split()
        ooc_name = 1
        for word in args:
            if word.lower().endswith(':'):
                break
            else:
                ooc_name += 1
        if ooc_name == len(args) + 1:
            raise ArgumentError('Invalid syntax. Add \':\' in the end of target.')
        poll = ' '.join(args[:ooc_name])
        poll = poll[:len(poll) - 1]
        choice = ' '.join(args[ooc_name:])
        if not choice:
            raise ArgumentError('Not enough arguments. Use /pollchoiceremove <poll>: <choice to be removed>.')
        x = client.server.serverpoll_manager.add_poll_choice(client, poll, choice)
        if x is None:
            return
        client.send_ooc(
            'Added {} as a choice in poll {}. Current choices:\n{} '.format(choice, poll, "\n".join(x)))
        database.log_misc('poll choice add', client, target=None, data=poll + choice)
    else:
        return

# this shit sucks, don't use it
@mod_only()
def ooc_cmd_makepollmulti(client, arg):
    """
    Allow multiple choice selections for a server poll, or return to a single choice vote.
    Usage: /makepollmulti <Poll Name>
    """
    if client.is_mod:
        x = client.server.serverpoll_manager.make_multipoll(arg)
        if x:
            client.send_ooc('Poll {} made multipoll.'.format(arg))
            database.log_misc('poll multi vote', client, target=None, data=arg)
        else:
            client.send_ooc('Poll {} made single poll.'.format(arg))
            database.log_misc('poll single vote', client, target=None, data=arg)
    else:
        return