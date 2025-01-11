### Ported from AOV tsuserver3; sorry if I fucked it up, Konig, miss u bb
### https://github.com/AttorneyOnlineVidya/tsuserver3

import json
import os
import time

import yaml

from server import database
from server import logger
from server.exceptions import ServerError


class ServerpollManager:
    def __init__(self, server):
        self.server = server
        self.poll_list = []
        self.poll_display = []
        self.current_poll = []
        self.load_poll_list()
        self.vote = []
        self.slots = []
        self.voting = 0
        self.voting_at = 0

    def load_poll_list(self):
        try:
            with open('storage/poll/polllist.json', 'r') as poll_list_file:
                self.poll_list = json.load(poll_list_file)
        except FileNotFoundError:
            if not os.path.exists('storage/poll/'):
                os.makedirs('storage/poll/')
            with open('storage/poll/polllist.json', 'w') as poll_list_file:
                json.dump([], poll_list_file)
            return
        except ValueError:
            return

    def write_poll_list(self):
        with open('storage/poll/polllist.json', 'w') as poll_list_file:
            json.dump(self.poll_list, poll_list_file)

    def show_poll_list(self):
        output = [item[0] for item in self.poll_list]
        return output

    def poll_number(self):
        return len(self.poll_list)

    def add_poll(self, value):
        test = time.strftime('%y-%m-%d %H%M-%S')
        if not ([item for item in self.poll_list if item[0] == value]):
            if len(self.poll_list) < self.server.config['poll_slots']:
                self.poll_list.append([value, test])
                tmp = time.strftime('%y-%m-%d %H:%M:%S')
                newfile = {
                    'name': value,
                    'polldetail': None,
                    'multivote': False,
                    'choices': ["Yes", "No"],
                    'votes': {"yes": 0, "no": 0},
                    'created': tmp,
                    'log': [],
                    'faillog': [],
                }
                with open('storage/poll/{} \'{}\'.yaml'.format(test, value), 'w') as file:
                    yaml.dump(newfile, file, default_flow_style=False)
            else:
                raise ServerError('The Poll Queue is full!')
        else:
            raise ServerError('This poll already exists.')
        self.write_poll_list()

    def remove_poll(self, value):
        if ([i for i in self.poll_list if i[0] == "{}".format(value)]):
            self.poll_list = [i for i in self.poll_list if i[0] != "{}".format(value)]
        elif value == "all":
            self.poll_list = []
        else:
            raise ServerError('The specified poll does not exist.')
        self.write_poll_list()

    def polldetail(self, value, detail):
        for i in self.poll_list:
            if i[0].lower() == value.lower():
                stream = open('storage/poll/{} \'{}\'.yaml'.format(i[1], i[0]), 'r')
                hold = yaml.safe_load(stream)
                hold['polldetail'] = detail
                write = open('storage/poll/{} \'{}\'.yaml'.format(i[1], i[0]), 'w')
                yaml.dump(hold, write, default_flow_style=False)
                return 1
        return 0

    def returndetail(self, value):
        for i in self.poll_list:
            if i[0].lower() == value.lower():
                stream = open('storage/poll/{} \'{}\'.yaml'.format(i[1], i[0]), 'r')
                hold = yaml.safe_load(stream)
                return hold['polldetail']

    def returnmulti(self, value):
        for i in self.poll_list:
            if i[0].lower() == value.lower():
                stream = open('storage/poll/{} \'{}\'.yaml'.format(i[1], i[0]), 'r')
                hold = yaml.safe_load(stream)
                return hold['multivote']

    def poll_exists(self, value):
        if [i for i in self.poll_list if i[0] == "{}".format(value)]:
            return True
        else:
            return False

    def load_votelist(self, value):
        if [i for i in self.poll_list if i[0] == "{}".format(value)]:
            poll_selected = [i[1] for i in self.poll_list if i[0] == "{}".format(value)]
            self.current_poll = ('{} \'{}\''.format("".join(poll_selected), value))
        else:
            return

    def get_votelist(self, value):
        try:
            if [i for i in self.poll_list if i[0] == "{}".format(value)]:
                poll_selected = [i[1] for i in self.poll_list if i[0] == "{}".format(value)]
                output = ('{} \'{}\''.format("".join(poll_selected), value))
                stream = open('storage/poll/{}.yaml'.format(output), 'r')
                stream2 = yaml.safe_load(stream)
                log = stream2['log']
                return log
            else:
                return None
        except FileNotFoundError:
            raise ServerError('The specified poll has no file associated with it.')
        except IndexError:
            raise ServerError('The poll list is currently empty.')

    def get_poll_choices(self, value):
        try:
            if [i for i in self.poll_list if i[0] == "{}".format(value)]:
                poll_selected = [i[1] for i in self.poll_list if i[0] == "{}".format(value)]
                output = ('{} \'{}\''.format("".join(poll_selected), value))
                stream = open('storage/poll/{}.yaml'.format(output), 'r')
                stream2 = yaml.safe_load(stream)
                choices = stream2['choices']
                return choices
            else:
                return None
        except FileNotFoundError:
            raise ServerError('The specified poll has no file associated with it.')
        except IndexError:
            return

    def clear_poll_choice(self, value):
        try:
            if [i for i in self.poll_list if i[0] == "{}".format(value)]:
                poll_selected = [i[1] for i in self.poll_list if i[0] == "{}".format(value)]
                output = ('{} \'{}\''.format("".join(poll_selected), value))
                stream = open('storage/poll/{}.yaml'.format(output), 'r')
                stream2 = yaml.safe_load(stream)
                stream2['choices'] = []
                stream2['votes'] = {}
                with open('storage/poll/{}.yaml'.format(output), 'w') as votelist_file:
                    yaml.dump(stream2, votelist_file, default_flow_style=False)
                return stream2['choices']
            else:
                return None
        except FileNotFoundError:
            raise ServerError('The specified poll has no file associated with it.')
        except IndexError:
            return

    def remove_poll_choice(self, client, value, remove):
        try:
            if [i for i in self.poll_list if i[0] == "{}".format(value)]:
                poll_selected = [i[1] for i in self.poll_list if i[0] == "{}".format(value)]
                output = ('{} \'{}\''.format("".join(poll_selected), value))
                stream = open('storage/poll/{}.yaml'.format(output), 'r')
                stream2 = yaml.safe_load(stream)
                choices = stream2['choices']
                if not remove in choices:
                    client.send_ooc('Item is not a choice.')
                    return
                stream2['choices'] = [x for x in choices if not x == remove]
                stream2['votes'].pop(remove.lower())
                with open('storage/poll/{}.yaml'.format(output), 'w') as votelist_file:
                    yaml.dump(stream2, votelist_file, default_flow_style=False)
                return stream2['choices']
            else:
                return None
        except FileNotFoundError:
            raise ServerError('The specified poll has no file associated with it.')
        except IndexError:
            return

    def add_poll_choice(self, client, value, add):
        try:
            if [i for i in self.poll_list if i[0] == "{}".format(value)]:
                poll_selected = [i[1] for i in self.poll_list if i[0] == "{}".format(value)]
                output = ('{} \'{}\''.format("".join(poll_selected), value))
                stream = open('storage/poll/{}.yaml'.format(output), 'r')
                stream2 = yaml.safe_load(stream)
                if add.lower() in [x.lower() for x in stream2['choices']]:
                    client.send_ooc('Item already a choice.')
                    return
                stream2['choices'].append(str(add))
                stream2['votes'][add.lower()] = 0
                with open('storage/poll/{}.yaml'.format(output), 'w') as votelist_file:
                    yaml.dump(stream2, votelist_file, default_flow_style=False)
                return stream2['choices']
            else:
                return None
        except FileNotFoundError:
            raise ServerError('The specified poll has no file associated with it.')
        except IndexError:
            return

    def make_multipoll(self, value):
        try:
            if [i for i in self.poll_list if i[0] == "{}".format(value)]:
                poll_selected = [i[1] for i in self.poll_list if i[0] == "{}".format(value)]
                output = ('{} \'{}\''.format("".join(poll_selected), value))
                stream = open('storage/poll/{}.yaml'.format(output), 'r')
                stream2 = yaml.safe_load(stream)
                stream2['multivote'] = not stream2['multivote']
                with open('storage/poll/{}.yaml'.format(output), 'w') as votelist_file:
                    yaml.dump(stream2, votelist_file, default_flow_style=False)
                return stream2['choices']
            else:
                return None
        except FileNotFoundError:
            raise ServerError('The specified poll has no file associated with it.')
        except IndexError:
            return

    def add_vote(self, value, vote, client):
        tmp = time.strftime('%y-%m-%d %H:%M:%S')
        try:
            # Open that shit up and extract the important parts.
            poll_voting = []
            for poll in self.poll_list:
                if poll[0].lower() == value.lower():
                    poll_voting = poll
                    break
            if not poll_voting:
                raise ServerError('Poll not found.')
            stream = open('storage/poll/{} \'{}\'.yaml'.format(poll_voting[1], poll_voting[0]), 'r')
            self.vote = yaml.safe_load(stream)
            log = self.vote["log"]
            pname = self.vote["name"]
            ipid_voted = self.check_ipid(log, client)
            hdid_voted = self.check_hdid(log, client)
            if (ipid_voted or hdid_voted) and (not self.vote['multivote']):
                # Now to log their failed vote
                self.vote['faillog'] += (['FAILED VOTE', tmp, client.ipid, client.hdid, vote,
                                      "{} ({}) at area {}".format(client.name, client.char_name,
                                                                  client.area.name)])
                self.write_votelist(poll_voting)
                database.log_area("vote failed", client, client.area, message=pname)
                client.send_ooc('Error: You have already voted in this poll.')
            # kill multivoting because it's not working right now because of this shit v
            #elif (ipid_voted or hdid_voted) and [item for item in log if item[3].lower() == vote.lower()]:
            #    self.vote['faillog'] += (['FAILED VOTE', tmp, client.ipid, client.hdid, vote,
            #                          "{} ({}) at area {}".format(client.name, client.char_name,
            #                                                      client.area.name)])
            #    self.write_votelist(poll_voting)
            #    database.log_area("vote failed", client, client.area, message=pname)
            #    client.send_ooc('Error: You have chosen this choice already.')
            else:
                # If they aren't a filthy rigger, they should get to this point
                if vote.lower() in [x.lower() for x in self.vote['choices']]:
                    self.vote['votes'][vote.lower()] += 1
                tmp = time.strftime('%y-%m-%d %H:%M:%S')
                self.vote['log'] += ([tmp, str(client.ipid), client.hdid, vote,
                                      "{} ({}) at area {}".format(client.name, client.char_name,
                                                                  client.area.name)])
                self.write_votelist(poll_voting)
                database.log_area("vote success", client, client.area, message=pname)
                client.send_ooc('You have successfully voted for {}! Thanks for voting.'.format(vote.capitalize()))
        except FileNotFoundError:
            database.log_area("vote failed", client, client.area, message=pname)
            client.send_ooc('Voting Error - Poll does not exist.')
            raise ServerError('The specified poll does not have a file associated with it.')
        except IndexError:
            # todo: A bit redundant. There's probably a better way.
            #if vote.lower() in [x.lower() for x in self.vote['choices']]:
            #    self.vote['votes'][vote.lower()] += 1
            tmp = time.strftime('%y-%m-%d %H:%M:%S')
            self.write_votelist(poll_voting)
            database.log_area("vote failed", client, client.area, message=pname)
            client.send_ooc('Error: IndexError.')
        client.send_ooc('=== Leaving Voting Mode... ===')

    def write_votelist(self, poll):
        with open('storage/poll/{} \'{}\'.yaml'.format(poll[1], poll[0]), 'w') as votelist_file:
            yaml.dump(self.vote, votelist_file, default_flow_style=False)
            #           Clear variables to default now that you're done writing.
            self.vote = []

    def check_ipid(self, log, client):
        voted = False
        ipid = str(client.ipid)
        #for item in log:
            #if item[1] == ipid: [this shit breaks and causes a disconnect so we try something else and pray]
        if any(ipid in item for item in log):
            voted = True
        return voted

    def check_hdid(self, log, client):
        voted = False
        hdid = client.hdid
        #for item in log: [same as above]
            #if item[2] == hdid:
        if any(hdid in item for item in log):
            voted = True
        return voted