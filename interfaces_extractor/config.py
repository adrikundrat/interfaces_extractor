import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_USERNAME = os.getenv('POSTGRES_USER', 'postgres')
DATABASE_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('POSTGRES_DB', 'extractor')

PATH_TO_FILE = os.getenv('PATH_TO_FILE', 'data/configClear_v2_updated.json')

NATIVE_FIELD_KEY = 'Cisco-IOS-XE-native:native'
CHANNEL_GROUP_KEY = 'Cisco-IOS-XE-ethernet:channel-group'
CHANNEL_GROUP_REFERENCE_KEY = 'number'
INTERFACE_KEY = 'interface'

BDI_KEY = 'BDI'
LOOPBACK_KEY = 'Loopback'
PORT_CHANNEL_KEY = 'Port-channel'
TEN_GIGABIT_ETHERNET_KEY = 'TenGigabitEthernet'
GIGABIT_ETHERNET_KEY = 'GigabitEthernet'

KEYS_FROM_ENV = os.getenv("KEYS_TO_DATABASE", None)

KEYS_TO_DATABASE = KEYS_FROM_ENV.split(",") if KEYS_FROM_ENV else [PORT_CHANNEL_KEY, TEN_GIGABIT_ETHERNET_KEY, GIGABIT_ETHERNET_KEY]