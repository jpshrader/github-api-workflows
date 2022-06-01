'''Helper functions for reading in data files'''
from typing import Any

import json
import yaml

JSON_FILE_TYPE = 'json'
YAML_FILE_TYPE = 'yaml'

def get_file(file: str, file_type: str) -> (Any | None):
    '''Deserialises a given file'''
    if file_type == JSON_FILE_TYPE:
        return get_json_file(file)
    if file_type == YAML_FILE_TYPE:
        return get_yaml_file(file)
    return None

def get_json_file(file: str) -> (Any | None):
    '''Deserialises a given json file'''
    with open(file, 'r', encoding='utf8') as stream:
        try:
            return json.load(stream)
        except json.JSONDecodeError as err:
            print(err)
    return None

def get_yaml_file(file) -> (Any | None):
    '''Deserialises a given yaml file'''
    with open(file, 'r', encoding='utf8') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return None

def get_data(data: str, file_type: str) -> (Any | None):
    '''Deserialises a given file'''
    if file_type == JSON_FILE_TYPE:
        return get_json_data(data)
    if file_type == YAML_FILE_TYPE:
        return get_yaml_data(data)
    return None

def get_json_data(data: str) -> (Any | None):
    '''Deserialises a given json string'''
    return json.load(data)

def get_yaml_data(data: str) -> (Any | None):
    '''Deserialises a given yaml string'''
    return yaml.safe_load(data)
