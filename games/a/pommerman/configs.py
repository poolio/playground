from . import envs
from . import characters

import gym

def ffa_v0():
    env = envs.v0.Pomme
    game_type = envs.utility.GameType.FFA
    env_entry_point = 'envs:v0:Pomme'
    env_id = 'Pomme-v0'
    env_kwargs = {
        'game_type': game_type,
        'board_size': envs.utility.BOARD_SIZE,
        'agent_view_size': envs.utility.AGENT_VIEW_SIZE,
        'num_rigid': envs.utility.NUM_RIGID,
        'num_wood': envs.utility.NUM_WOOD,
        'num_items': envs.utility.NUM_ITEMS,
        'max_steps': envs.utility.MAX_STEPS
    }
    agent = characters.Agent
    return locals()


def ffa_v1():
    env = envs.v1.Pomme
    game_type = envs.utility.GameType.FFA
    env_entry_point = 'envs:v1:Pomme'
    env_id = 'Pomme-v1'
    env_kwargs = {
        'game_type': game_type,
        'board_size': envs.utility.BOARD_SIZE,
        'agent_view_size': envs.utility.AGENT_VIEW_SIZE,
        'num_rigid': envs.utility.NUM_RIGID,
        'num_wood': envs.utility.NUM_WOOD,
        'num_items': envs.utility.NUM_ITEMS,
        'first_collapse': envs.utility.FIRST_COLLAPSE,
        'max_steps': envs.utility.MAX_STEPS
    }
    agent = characters.Agent
    return locals()


def team_v0():
    env = envs.v0.Pomme
    game_type = envs.utility.GameType.Team
    env_entry_point = 'envs:v0:Pomme'
    env_id = 'Pomme-v0'
    env_kwargs = {
        'game_type': game_type,
        'board_size': envs.utility.BOARD_SIZE,
        'agent_view_size': envs.utility.AGENT_VIEW_SIZE,
        'num_rigid': envs.utility.NUM_RIGID,
        'num_wood': envs.utility.NUM_WOOD,
        'num_items': envs.utility.NUM_ITEMS,
        'max_steps': envs.utility.MAX_STEPS
    }
    agent = characters.Agent
    return locals()


def radio_v2():
    env = envs.v2.Pomme
    game_type = envs.utility.GameType.TeamRadio
    env_entry_point = 'envs:v0:Pomme'
    env_id = 'Pomme-v0'
    env_kwargs = {
        'game_type': game_type,
        'board_size': envs.utility.BOARD_SIZE,
        'agent_view_size': envs.utility.AGENT_VIEW_SIZE,
        'num_rigid': envs.utility.NUM_RIGID,
        'num_wood': envs.utility.NUM_WOOD,
        'num_items': envs.utility.NUM_ITEMS,
        'max_steps': envs.utility.MAX_STEPS
    }
    agent = characters.Agent
    return locals()
