# from django.db import models

# Create your models here.
from dataclasses import dataclass
from typing import List, Optional
import json

@dataclass
class TeamMember:
    name: str
    email: str
    team: str
    role: str
    picture: Optional[str] = None

    @classmethod
    def load_from_json(cls, filepath: str) -> List["TeamMember"]:
        with open(filepath, 'r') as f:
            team_members_data = json.load(f)

        return [cls(**member) for member in team_members_data]