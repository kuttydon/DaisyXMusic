# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "InfinityMusic")
BOT_TOKEN = getenv("BOT_TOKEN", "5020827600:AAEW8TrCxLmnsMlUEwVukaHjOci2znkGXqg")
BOT_NAME = getenv("BOT_NAME", "Infinity Music 🎶")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Tamil_Love_Beats")
BG_IMAGE = getenv("BG_IMAGE", "")
admins = {}
API_ID = int(getenv("API_ID", "9198225"))
API_HASH = getenv("API_HASH", "952faef610dec9240fafd4e3a8ce1536")
BOT_USERNAME = getenv("BOT_USERNAME", "Infinity_Musiq_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Infinity_Assist")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "TLB_Comments")
PROJECT_NAME = getenv("PROJECT_NAME", "InfinityMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "ZVKWOO-XDYPHI-XTYRYK-KHUQQU-ARQ")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
