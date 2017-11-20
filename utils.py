import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from time import sleep

# Need to load an api-key
api_key = '646928682c4b5d6f5f6c782a6b351b29'


def get_all_groups(location_str, radius=25, write_path=None, api_key=api_key):
    '''Gets a list of all groups within a set radius from a location. Returns a dataframe.'''
    cols = ('group_id', 'group_name', 'num_members', 'category_id', 
            'category_name', 'organizer_id', 'group_urlname')
    all_groups = pd.DataFrame(columns=cols)

    for page in np.arange(10):
        q = 'https://api.meetup.com/find/groups?&sign=true&location={}&radius={}&page=200&offset={}'.format(location_str, radius, page)
        q += '&key={}'.format(api_key) 
        response = requests.get(q).json()
        if len(response) > 0:
            try:
                for g in response:
                    s = pd.Series((g['id'], g['name'], g['members'], g['category']['id'], 
                                   g['category']['name'], g['organizer']['id'], g['urlname']),
                                 index=cols)
                    all_groups = all_groups.append(s, ignore_index=True)
            except KeyError as exc:
                print(g['name'], exc)
        # Sleep briefly so that API doesn't get overwhelmed
        sleep(0.2)

    all_groups = all_groups.astype({'group_id': int, 'organizer_id': int, 'category_id': int, 'num_members': int})
    all_groups = all_groups.set_index('group_id')
    
    # Write to computer
    if write_path:
        all_groups.to_csv(write_path, encoding='utf-8') 

    return all_groups


def get_group_members(group_id, api_key):
    '''Accepts a Meetup group ID number and returns dataframe with all members in the group.'''
    # Initialize variables
    members = pd.DataFrame()
    page = 0
    bad_iters = 0
    
    # Keep querying until there are no more results
    all_results = False
    while all_results == False:
        q = 'https://api.meetup.com/2/members?'
        q += '&sign=true&group_id={}&only=name,id,city,state,hometown,joined,visited,lat,lon&page=200&offset={}'.format(group_id, page)
        q += '&key={}'.format(api_key)
        response = requests.get(q).json()
        if 'results' in response.keys():
            if len(response['results']) == 0:
                all_results = True
            try:
                tdf = pd.DataFrame.from_dict(response['results'])
                members = members.append(tdf)
                page += 1
            except KeyError as exc:
                all_results = True
                bad_iters += 1
                if bad_iters > 5:
                    all_results=True
                pass
            except json.decoder.JSONDecodeError:
                bad_iters += 1
                if bad_iters > 5:
                    all_results=True
                pass

    members['group_id'] = group_id
    
    return members


def agg_group_members(list_of_group_ids, api_key, write_path=None, intermediate_path=None):
    '''Retrieves member data for a list of MeetUp groups. Returns a dataframe with this information.'''
    all_members = pd.DataFrame()
    
    for g in list_of_group_ids:
        sleep(1)
        try:
            tdf = get_group_members(g, api_key)
            if intermediate_path:
                tdf.to_csv('{}/{}.csv'.format(intermediate_path, g), encoding='utf-8')
            all_members = all_members.append(tdf)
        except KeyError as exc:
            print(group, exc)
            continue

    # Write to computer
    if write_path:
        #for date_col in ['joined', 'visited']:
            #    members[date_col] = pd.to_datetime(members[date_col], unit='ms')
        all_members.to_csv(write_path, encoding='utf-8') 
        
    return all_members


def get_events(urlname, date_filter_str=None, api_key=api_key):
    ''' Takes a Meetup group urlname and returns a DataFrame of events. Optionally, filter by date.'''
    
    q = 'https://api.meetup.com/{}/events?'.format(urlname)
    q += '&sign=true&page=200&status=past&only=id,name,status,time,yes_rsvp_count&desc=True'
    q += '&{}'.format(api_key)
    response = requests.get(q)
    if response.status_code == 410:
        raise ValueError('Group not accessible.')
    if len(response.json()) == 0:
        raise ValueError('No event results.')
    
    events_df = pd.DataFrame.from_dict(response.json())
    events_df.time = pd.to_datetime(events_df.time, unit='ms')
    events_df['group_urlname'] = urlname
    
    if date_filter_str:
        events_df = events_df.loc[events_df.time > pd.to_datetime(date_filter_str)]
    
    return events_df
    
    
def get_event_rsvps(urlname, event_id, api_key=api_key):
    '''Accepts a group urlname and event id, and returns a dataframe of RSVPs.'''
    q = 'https://api.meetup.com/{}/events/{}/rsvps?'.format(urlname, event_id)
    q += '&sign=true&photo-host=public&response=yes&only=member'
    q += '&{}'.format(api_key)
    response = requests.get(q).json()
    member_list = [(urlname, event_id, mem['member']['id']) for mem in response]
    rsvp_df = pd.DataFrame(member_list, columns=['group_urlname', 'event_id', 'member_id'])
    return rsvp_df


def get_all_event_rsvps(urlname, list_of_event_ids, api_key):
    '''Accepts a group urlname and list of event ids, and returns a DataFrame of RSVPs. '''
    all_rsvp_df = pd.DataFrame(columns=['group_urlname', 'event_id', 'member_id'])
    for eid in list_of_event_ids:
        tdf = get_event_rsvps(urlname, eid, api_key)
        all_rsvp_df = all_rsvp_df.append(tdf, ignore_index=True)
    
    return all_rsvp_df


def setup_graph_plot(**kwargs):
    '''Creates an empty figure with one axis and requested input arguments. Removes the axis frame and sets X-Y aspect ratios to be equal. Returns a Matplotlib Figure and Axis object. '''
    fig, ax = plt.subplots(1,1, **kwargs)

    # Other graph settings
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_aspect(1)
    ax.set_frame_on(False)
    
    return fig, ax